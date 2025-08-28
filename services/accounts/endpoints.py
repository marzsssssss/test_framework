import os

class Endpoints:

    total_amount = lambda self, cur_id: f"{os.getenv('HOST')}/accounts/total-amount/{cur_id}/"

    get_accounts_ewallet = f"{os.getenv('HOST')}/accounts/ewallets/"

    get_ewallet_currencies = f"{os.getenv('HOST')}/accounts/ewallets/currencies/"

    get_entity_ewallets = lambda self, cur_id: f"{os.getenv('HOST')}/accounts/ewallets/{cur_id}/"

    create_entity_ewallet = f"{os.getenv('HOST')}/accounts/ewallets/"