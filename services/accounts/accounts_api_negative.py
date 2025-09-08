import requests
import allure 

from utils.helper import Helper 
from services.accounts.endpoints import Endpoints

class AccountsNegativeAPI(Helper):

    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()

    @allure.step('Total Amount User Negative')
    def total_amount_negative(self, headers, expected_status,uuid):
        response = requests.get(
            url = self.endpoints.total_amount(uuid),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
        
    @allure.step('Get Accounts Ewallet Negative')
    def get_accounts_ewallet_negativ(self, headers, expected_status):
        response = requests.get(
            url = self.endpoints.get_accounts_ewallet,
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
    
    @allure.step('Get Ewallet Currencies Negative')
    def get_ewallet_currencies(self, headers, expected_status):
        response = requests.get(
            url = self.endpoints.get_ewallet_currencies,
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)

    @allure.step('Get Entity Ewallets Negative')
    def get_entity_ewallets(self, headers, expected_status, uuid):
        response = requests.get(
            url = self.endpoints.get_entity_ewallets(uuid),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
    
    @allure.step('Create Entity Ewallet Negative')
    def create_entity_ewallet(self,headers, expected_status, uuid):
        response = requests.post(
            url=self.endpoints.create_entity_ewallet,
            headers = headers,
            json = {"currency_id": uuid}
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)