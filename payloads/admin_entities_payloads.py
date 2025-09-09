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
    
    #Required 
    @staticmethod
    def without_field(field, ewallet_id):
        payload = Payloads.adjust_balance(ewallet_id)
        payload_copy = payload.copy()
        payload_copy.pop(field, None)
        return payload_copy