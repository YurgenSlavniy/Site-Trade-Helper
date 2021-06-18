
class BaseConf:
    pass


class DevConf(BaseConf):
    DEBUG = True
    HOSTNAME = 'localhost'
    USERNAME = 'my-name'
    PASSWORD = 'my-password'
    DBNAME = 'my-database'
    CHARSET = 'utf8mb4'


class TestConf(BaseConf):
    pass


class ProdConf(BaseConf):
    pass
