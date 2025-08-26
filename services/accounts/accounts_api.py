import requests
import allure 

from utils.helper import Helper 
from services.accounts.endpoints import Endpoints
from core.headers import Headers
from payloads.accounts_payloads import Payloads
from models.accounts_model import AccountsModel
from models.accounts_model import CreateEntityEwallet

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
        self.attach_response(response.json())
        return model
        
    @allure.step('Get Accounts Ewallet')
    def get_accounts_ewallet(self):
        response = requests.get(
            url = self.endpoints.get_accouts_ewallet,
            headers=self.headers.basic
        )
        self.assert_response(response)
        self.attach_response(response.json())
        return response.json()
    
    @allure.step('Get Ewallet Currencies')
    def get_ewallet_currencies(self):
        response = requests.get(
            url = self.endpoints.get_ewallet_currencies,
            headers=self.headers.basic
        )
        self.assert_response(response)
        self.attach_response(response.json())
        return response.json()

    @allure.step('Get Entity Ewallets')
    def get_entity_ewallets(self,uuid):
        response = requests.get(
            url = self.endpoints.get_entity_ewallets(uuid),
            headers=self.headers.basic
        )
        self.assert_response(response)
        self.attach_response(response.json())
        return response.json()
    
    @allure.step('Create Entity Ewallet')
    def create_entity_ewallet(self,uuid):
        response = requests.post(
            url=self.endpoints.create_entity_ewallet,
            headers = self.headers.basic,
            json = self.payloads.entity_ewallet(uuid)
        )
        self.assert_response(response)
        model = CreateEntityEwallet(**response.json())
        self.attach_response(response.json())
        return model