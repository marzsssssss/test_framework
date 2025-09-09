import requests 
import allure

from utils.helper import Helper
from services.admin_entities.endpoints import Endpoints
from core.headers import Headers
from payloads.admin_entities_payloads import Payloads
from models.admin_entities_model import GetEntitiesModel



class AdminEntitiesAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()
        self.payloads = Payloads()


    @allure.step('Admin - Get Entities Accounts List')    
    def get_entities_accounts_list(self,name):
        response = requests.get(
            url = self.endpoints.get_entities_accounts_list(name),
            headers=self.headers.basic
        )
        self.assert_response(response)
        model = GetEntitiesModel(**response.json())
        self.attach_response_to_allure(response)
        return model
    
    @allure.step('Admin - POST Entities Accounts adjust balance')   
    def post_entities_accouts_adjust_balance(self, get_ewallet_id):
        response = requests.post(
            url = self.endpoints.post_entities_accouts_adjust_balance,
            headers = self.headers.basic,
            json = self.payloads.adjust_balance(get_ewallet_id)
        )
        self.assert_create_response(response)