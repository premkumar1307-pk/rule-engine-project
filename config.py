import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://rule_engine_user:your_password@localhost/rule_engine_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
