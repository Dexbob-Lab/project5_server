import os, json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

def getEnvValue(key):
    BASE_DIR = Path(__file__).resolve().parent.parent
    try:
        secret_file = os.path.join(BASE_DIR, 'env.json')
        with open(secret_file) as f:
            secrets = json.loads(f.read())
        return secrets[key]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {key} environment variable")


# SECRET_KEY = getEnvValue("SECRET_KEY")

# env.json
# {
#     "SECRET_KEY": "키값"
# }