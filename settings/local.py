import os

# DDEV automatically provides DB credentials for the 'db' container in environment variables
# named DDEV_DB_*, or standard POSTGRES_* if using the postgres image type.
# However, DDEV's internal hostname for the db is always "db".

# We map DDEV defaults to Mage2Gen's expected "MYSQL_" variable names
# (Mage2Gen uses 'MYSQL_' keys even for Postgres config in base.py)

MYSQL_DB = os.environ.get('MAGE2GEN_DB_NAME', 'db')
MYSQL_USERNAME = os.environ.get('MAGE2GEN_DB_USER', 'db')
MYSQL_PASSWORD = os.environ.get('MAGE2GEN_DB_PASS', 'db')
MYSQL_HOST = os.environ.get('MAGE2GEN_DB_HOST', 'db')
MYSQL_PORT = os.environ.get('MAGE2GEN_DB_PORT', '5432')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-default-dev-key')
# Use 0 for False, 1 for True
USE_SQLITE = int(os.environ.get('USE_SQLITE', 0))

# Generation Path
MODULE_GENERATION_PATH = os.environ.get('MODULE_GENERATION_PATH', '/usr/app/src/generated_modules')

# Ensure path exists
try:
    if not os.path.exists(MODULE_GENERATION_PATH):
        os.makedirs(MODULE_GENERATION_PATH)
except Exception:
    pass