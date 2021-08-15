from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("LE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config('LE_SECRET_KEY', cast=str,
                    default="bc127b181d85b8c1911ffd4d687f42b59ee75c85f41fe89e06b89336e274e1ec")

