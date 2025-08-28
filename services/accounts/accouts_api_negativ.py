import requests
import allure 

from utils.helper import Helper 
from services.accounts.endpoints import Endpoints

class AccountsNegativAPI(Helper):

    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()

    @allure.step('Total Amount User Negativ')
    def total_amount_negativ(self, headers, expected_status,uuid):
        response = requests.get(
            url = self.endpoints.total_amount(uuid),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response(response.json())
        
    @allure.step('Get Accounts Ewallet Negativ')
    def get_accounts_ewallet_negativ(self, headers, expected_status):
        response = requests.get(
            url = self.endpoints.get_accouts_ewallet,
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response(response.json())
    
    @allure.step('Get Ewallet Currencies Negativ')
    def get_ewallet_currencies(self, headers, expected_status):
        response = requests.get(
            url = self.endpoints.get_ewallet_currencies,
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response(response.json())

    @allure.step('Get Entity Ewallets Negativ')
    def get_entity_ewallets(self, headers, expected_status, uuid):
        response = requests.get(
            url = self.endpoints.get_entity_ewallets(uuid),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response(response.json())
    
    @allure.step('Create Entity Ewallet Negativ')
    def create_entity_ewallet(self,headers, expected_status, uuid):
        response = requests.post(
            url=self.endpoints.create_entity_ewallet,
            headers = headers,
            json = uuid
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response(response.json())