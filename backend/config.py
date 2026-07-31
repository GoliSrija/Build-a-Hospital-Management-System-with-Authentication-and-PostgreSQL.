```python
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```