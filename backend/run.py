import sys
from app import create_app
from config import app_config, app_active
from flask_mqtt import Mqtt

config = app_config[app_active]
config.APP = create_app(app_active)
mqtt = Mqtt(app)

if __name__ == '__main__':
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    
    reload(sys)