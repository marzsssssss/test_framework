from faker import Faker

fake = Faker()


class Payloads:

    @staticmethod
    def adjust_balance(ewallet_id):
        return {
            "invoice_direction": "SEND",
            "account_ewallet_id": ewallet_id,
            "amount": fake.random_int(min=50,max=100),
            "hidden": fake.boolean
            }