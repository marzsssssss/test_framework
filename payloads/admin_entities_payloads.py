from faker import Faker

fake = Faker()


class Payloads:

    @staticmethod
    def adjust_balance(ewallet_id):
        return {
            "invoice_direction": "SEND",
            "account_ewallet_id": ewallet_id,
            "amount": fake.random_int(min=50, max=100),
            "hidden": fake.boolean()
        }
    
    #Обязательные поля
    @staticmethod
    def without_field(field, ewallet_id):
        payload = Payloads.adjust_balance(ewallet_id)
        payload_copy = payload.copy()
        payload_copy.pop(field, None)
        return payload_copy
    
    @staticmethod
    def field_test(field, ewallet_id):
        payload = Payloads.adjust_balance(ewallet_id)
        payloads = []

       
        negative_values = {
            "invoice_direction": [
                fake.pystr(min_chars=4, max_chars=4), 
                fake.random_number(digits=3),                                       
            ],
            "account_ewallet_id": [          
                fake.random_number(digits=3),
                fake.boolean()           
            ],
            "amount": [
                -10,                                   
                "ten",                                  
                0,                                       
            ],
            "hidden": [                                  
                "ten",                                  
                fake.uuid4(),
                '123'                                       
            ]
        }

        for value in negative_values.get(field, []):
            pl = payload.copy()
            pl[field] = value
            payloads.append(pl)

        return payloads