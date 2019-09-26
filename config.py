class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///addsiProd.db'
    SQLALCHEMY_BINDS = {
        'meldungen': 'mysql+pymysql://can_read@localhost/meldungen'
    }

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://can_write@localhost/metabot'
    SQLALCHEMY_BINDS = {
        'meldungen': 'mysql+pymysql://can_read@localhost/meldungen'
    }
    ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///addsiTest.db'
    SQLALCHEMY_BINDS = {
        'meldungen': 'sqlite:///meldungenTest.db'
    }
    DEBUG = True
    TESTING = True