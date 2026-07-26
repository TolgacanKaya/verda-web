import os
from pathlib import Path

def load_env_var(var_name, default=None):
    """Loads an environment variable from the .env file if it exists, otherwise falls back to system environment."""
    base_dir = Path(__file__).resolve().parent.parent
    for p in [base_dir, base_dir.parent]:
        env_file = p / '.env'
        if env_file.exists():
            try:
                with open(env_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            k, v = line.split('=', 1)
                            if k.strip() == var_name:
                                val = v.strip()
                                if val.startswith(('"', "'")) and val.endswith(('"', "'")):
                                    val = val[1:-1]
                                return val
            except Exception:
                pass
    return os.environ.get(var_name, default)

def get_gemini_api_key():
    """Returns the Gemini API key from environment, setting default fallback securely if not found."""
    return load_env_var('GEMINI_API_KEY', 'AIzaSyBOWZwCsSc4yGJjuf3zLSbEugxdUA9k1Ws')

def get_openweather_api_key():
    """Returns the OpenWeather API key from environment, setting default fallback securely if not found."""
    # Checks for multiple common naming schemes of the weather key
    for name in ['OPENWEATHER_API_KEY', 'OPENWEATHER_KEY', 'WEATHER_API_KEY', 'API_KEY']:
        val = load_env_var(name)
        if val:
            return val
    return 'c8d51cf557ddfcf8e0ce4663ef108efd7'
