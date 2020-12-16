# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import func
from config import app_config, app_active
from model.User import User

config = app_config[app_active]

db = SQLAlchemy(config.APP)

config = app_config[app_active]

db = SQLAlchemy(config.APP)

class Device(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),unique=True,nullable=False)
    description=db.Column(db.Text(),nullable=False)
    ip=db.Column(db.String(15),nullable=False)
    ip_broker=db.Column(db.String(15),nullable=False)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
    last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=False)
    status=db.Column(db.Boolean(),default=1,nullable=True)
    user_created=db.Column(db.Integer,db.ForeignKey(User.id),nullable=False)
    usuario=relationship(User)

    def get_all():
        try:
            res = db.session.query(Device).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False
    
    def update(self, obj):
        try:
            res = db.session.query(Device).filter(Device.id == self.id).update(obj)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def get_total_devices(self):
        try:
            res = db.session.query(func.count(Device.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def get_last_devices(self):
        try:
            res = db.session.query(Device).order_by(Device.date_created).limit(5).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def get_all(self, limit):
        try:
            if limit is None:
                res = db.session.query(Device).all()
            else:
                res = db.session.query(Device).order_by(Device.date_created).limit(limit).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_device_by_id(self):
        try:
            res = db.session.query(Device).filter(Device.id==self.id).first()
        except Exception as e:
            res = None
            print(e)
        finally:
            db.session.close()
            return res
    
    def __repr__(self):
        return self.name