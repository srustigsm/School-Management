import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:Nive@203005@classconnect")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
