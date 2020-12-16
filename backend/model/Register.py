# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import func
from config import app_config, app_active
from model.Device import Device

config = app_config[app_active]

db = SQLAlchemy(config.APP)

class Register(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    topico=db.Column(db.String(15),nullable=True)
    date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=True)
    value=db.Column(db.String(25),nullable=True)
    responsible_device=db.Column(db.Integer,db.ForeignKey(Device.id),nullable=True)
    device=relationship(Device)

    def get_all():
        try:
            res = db.session.query(Register).all()
        except Exception as e:
            print(e)
            res = []
            
        finally:
            db.session.close()
            return res
    
    def get_total_registers(self):
        try:
            res = db.session.query(func.count(Register.id)).first()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def get_last_registers(self):
        try:
            res = db.session.query(Register).order_by(Register.date_created).limit(5).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
    
    def get_all(self, limit):
        try:
            if limit is None:
                res = db.session.query(Register).all()
            else:
                res = db.session.query(Register).order_by(Register.date_created).limit(limit).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res
        
    def get_register_by_id(self):
        try:
            res = db.session.query(Register).filter(Register.id==self.id).first()
        except Exception as e:
            res = None
            print(e)
        finally:
            db.session.close()
            return res

    def __repr__(self):
        return self.name