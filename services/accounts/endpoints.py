import os

class Endpoints:

    total_amount = lambda self, cur_id: f"{os.getenv('HOST')}/accounts/total-amounts/{cur_id}/"

    accouts_ewallet = f"{os.getenv('HOST')}/accounts/ewallets/"

    ewallet_currencies = f"{os.getenv('HOST')}/accounts/ewallets/currencies/"

    entity_ewallets = lambda self, cur_id: f"{os.getenv('HOST')}/ewallets/{cur_id}/"

    create_entity_ewallet = f"{os.getenv('HOST')}/accounts/ewallets"