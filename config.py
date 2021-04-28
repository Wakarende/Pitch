import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql://zokrmsetlfbeai:835f998ecde6aedc0d50af1cb0025c0270bb8af8ce688c41243b5897df430797@ec2-3-217-219-146.compute-1.amazonaws.com:5432/d64qef7sr4q4ed?sslmode=require"

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joykirii:kirii@localhost/pitch'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}