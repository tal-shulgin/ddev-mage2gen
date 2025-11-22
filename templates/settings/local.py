import os
MYSQL_DB = os.environ.get('MAGE2GEN_DB_NAME', 'db')
MYSQL_USERNAME = os.environ.get('MAGE2GEN_DB_USER', 'db')
MYSQL_PASSWORD = os.environ.get('MAGE2GEN_DB_PASS', 'db')
MYSQL_HOST = os.environ.get('MAGE2GEN_DB_HOST', 'db')
MYSQL_PORT = os.environ.get('MAGE2GEN_DB_PORT', '5432')
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-default-dev-key')
USE_SQLITE = int(os.environ.get('USE_SQLITE', 0))
MODULE_GENERATION_PATH = os.environ.get('MODULE_GENERATION_PATH', '/usr/app/src/generated_modules')
try:
    if not os.path.exists(MODULE_GENERATION_PATH):
        os.makedirs(MODULE_GENERATION_PATH)
except Exception:
    pass