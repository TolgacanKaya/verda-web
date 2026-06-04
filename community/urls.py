from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('gonderi/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('gonderi/<int:pk>/sil/', views.delete_post_view, name='delete_post'),
    path('bildirimler/', views.notifications_view, name='notifications'),
    path('api/bildirimler/', views.get_notifications_api, name='get_notifications_api'),
    path('api/bildirimleri-okundu-isaretle/', views.mark_all_read_api, name='mark_all_read_api'),
    path('api/feed/', api_views.community_api, name='community_api'),
    path('api/yorum-yap/', api_views.comment_api, name='comment_api'),
]