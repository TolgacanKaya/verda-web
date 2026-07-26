import torch
import cv2
import numpy as np
from PIL import Image
from torchvision import transforms
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget
from pytorch_grad_cam.utils.image import show_cam_on_image
import os
from django.conf import settings
import uuid

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.models.custom_cnn import CustomPlantNet
from src.models.transfer_nets import TransferEfficientNetB0, TransferMobileNetV2


class AIProcessor:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # her telefondan bağlanan için baştan okumasın cache de tutuyorum
        self._model_cache = {}

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    # güvenli arka plan silici web tarafı için
    def remove_background_safe(self, image_pil):
        img = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
        h, w = img.shape[:2]
        new_w, new_h = 256, 256
        img_resized = cv2.resize(img, (new_w, new_h))

        mask = np.zeros(img_resized.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # kenarlarda yüzde onluk boşluklar
        margin_w = int(new_w * 0.1)
        margin_h = int(new_h * 0.1)
        rect = (margin_w, margin_h, new_w - 2 * margin_w, new_h - 2 * margin_h)

        cv2.grabCut(img_resized, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        result_img = img_resized * mask2[:, :, np.newaxis]

        # kullanıcı duvar çekerse diye tamamen siyah çıkarsa orjinali kullan
        if cv2.countNonZero(cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)) < (new_w * new_h * 0.10):
            result_img = img_resized

        return cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)

    def load_model(self, model_choice):
        # bellekte var mı diye bakıyorum 
        if model_choice in self._model_cache:
            return self._model_cache[model_choice]

        # bir üst klasördeki ağırlık dosyalarımıza gidiyoruz
        base_path = os.path.join(settings.BASE_DIR, '../saved_models/')

        if model_choice == 'efficientnet':
            model = TransferEfficientNetB0(num_classes=15)
            model_path = os.path.join(base_path, 'best_EfficientNetB0.pth')
            target_layers = [model.model.features[-1]]
        elif model_choice == 'mobilenet':
            model = TransferMobileNetV2(num_classes=15)
            model_path = os.path.join(base_path, 'best_MobileNetV2.pth')
            target_layers = [model.model.features[-1]]
        else:  
            model = CustomPlantNet(num_classes=15)
            model_path = os.path.join(base_path, 'best_Custom_CNN_Kral.pth')
            target_layers = [model.layer4[-1]]

        model.load_state_dict(torch.load(model_path, map_location=self.device, weights_only=True))
        model.to(self.device).eval()
        
        # daha sonra direk dönsün diye cache kaydettim
        self._model_cache[model_choice] = (model, target_layers)
        return model, target_layers

    def process(self, image_path, model_choice):
        original_pil = Image.open(image_path).convert("RGB")

        # önce temizle
        nobg_array = self.remove_background_safe(original_pil)
        nobg_pil = Image.fromarray(nobg_array)

        # üst üste binmesin isimler diye uuid kullandım
        unique_id = str(uuid.uuid4())[:8]
        nobg_filename = f"nobg_{unique_id}.jpg"
        nobg_path = os.path.join(settings.MEDIA_ROOT, nobg_filename)
        nobg_pil.save(nobg_path)
        nobg_url = f"{settings.MEDIA_URL}{nobg_filename}"

        # modele sorma evresi
        model, target_layers = self.load_model(model_choice)
        input_tensor = self.transform(nobg_pil).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = model(input_tensor)
            probs = torch.nn.functional.softmax(outputs, dim=1)[0]
            class_id = outputs.argmax(dim=1).item()
            confidence = probs[class_id].item() * 100

        # neden o hastalık dedi diye ısı haritası
        cam = GradCAM(model=model, target_layers=target_layers)
        targets = [ClassifierOutputTarget(class_id)]
        grayscale_cam = cam(input_tensor=input_tensor, targets=targets)[0, :]

        rgb_img_float = np.float32(nobg_pil.resize((224, 224))) / 255.0
        heatmap_array = show_cam_on_image(rgb_img_float, grayscale_cam, use_rgb=True)
        heatmap_pil = Image.fromarray(heatmap_array)

        heatmap_filename = f"heatmap_{unique_id}.jpg"
        heatmap_path = os.path.join(settings.MEDIA_ROOT, heatmap_filename)
        heatmap_pil.save(heatmap_path)
        heatmap_url = f"{settings.MEDIA_URL}{heatmap_filename}"

        return class_id, confidence, nobg_url, heatmap_url