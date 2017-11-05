# coding: utf-8


class Config(object):
    ALLOW_ORIGINS = []
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    ALLOW_ORIGINS = [
        'http://localhost:8080',
    ]
    DEBUG = True


class StagingConfig(Config):
    ALLOW_ORIGINS = [
        'https://ubie-staging.appspot.com',
    ]


class ProductionConfig(Config):
    ALLOW_ORIGINS = [
        'https://ubie-production.appspot.com',
    ]
