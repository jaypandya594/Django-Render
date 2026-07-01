import dj_database_url
from decouple import config

# Reads Coolify's unified connection string directly
DATABASE_URL = config('DATABASE_URL', default='')

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    # Safe local fallback so your code doesn't crash if envs are missing locally
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
