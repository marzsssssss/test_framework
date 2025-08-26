import requests
import allure 

from utils.helper import Helper 
from services.accounts.endpoints import Endpoints
from core.headers import Headers
from payloads.accounts_payloads import Payloads
from models.accounts_model import AccountsModel


class AccountsAPI(Helper):

    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()

    @allure.step('Total Amount User')
    def total_amount(self, uuid):
        response = requests.get(
            url = self.endpoints.total_amount(uuid),
            headers=self.headers.basic,
        )
        self.assert_response(response)
        model = AccountsModel(**response.json())
        self.attach_respons(**response.json())
        return model
        