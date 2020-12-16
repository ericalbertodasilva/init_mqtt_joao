from datetime import datetime
from model.Device import Device

class DeviceController():
    def __init__(self):
        self.device_model = Device()

    def save_device(self, obj):
        self.device_model.name = obj['name']
        self.device_model.description = obj['description']
        self.device_model.ip = obj['ip']
        self.device_model.date_created = datetime.now()
        self.device_model.status = 1
        self.device_model.user_created = obj['user_created']
        return self.device_model.save()
    
    def update_device(self, obj):
        self.device_model.id = obj['id']
        return self.device_model.update(obj)
    
    def get_devices(self, limit):
        result = []
        try:
            res = self.device_model.get_all(limit=limit)
            for r in res:
                result.append({
                    'id': r.id,
                    'name': r.name,
                    'description': r.description,
                    'ip': r.ip,
                    'date_created': r.date_created
                })
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
            'result': result,
            'status': status
            }
    
    def get_device_by_id(self, device_id):
        result = {}
        try:
            self.device_model.id = device_id
            res = self.device_model.get_device_by_id()
            result = {
                'id': res.id,
                'name': res.name,
                'description': res.description,
                'ip': res.ip,
                'date_created': res.date_created
            }
            status = 200
        except Exception as e:
            print(e)
            result = []
            status = 400
        finally:
            return {
                'result': result,
                'status': status
            }
