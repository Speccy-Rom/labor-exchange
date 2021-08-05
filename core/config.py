from starlette.config import Config

config = Config()

DATABASE_URL = config("LE_DATABASE_URL", cast=str, default='')
