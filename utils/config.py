class DevelopmentConfig():
    debug = True
    SQLALCHEMY_DATABASE_URI="mysql://root:12345678@127.0.0.1:3306/erp"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
config = {
    'development': DevelopmentConfig
}