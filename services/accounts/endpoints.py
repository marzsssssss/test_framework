import os

class Endpoints:

    total_amount = lambda self, cur_id: f"{os.getenv('HOST')}/accounts/total-amounts/{cur_id}"
    accouts_ewallet = f"{os.getenv('HOST')}/accounts/ewallets/"