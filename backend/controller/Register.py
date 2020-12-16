from datetime import datetime
from model.Register import Register

class RegisterController():
    def __init__(self):
        self.register_model = Register()
    
    def get_registers(self, limit):
        result = []
        try:
            res = self.register_model.get_all(limit=limit)
            for r in res:
                result.append({
                    'id': r.id,
                    'topico': r.topico,
                    'value': r.value,
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
    
    def get_register_by_id(self, register_id):
        result = {}
        try:
            self.register_model.id = register_id
            res = self.register_model.get_register_by_id()
            result = {
                'id': res.id,
                'topico': res.topico,
                'value': res.value,
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