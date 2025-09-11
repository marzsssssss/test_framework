import httpx
import allure 
import pytest

from utils.helper import Helper 
from services.accounts.endpoints import Endpoints

class AccountsNegativeAPI(Helper):

    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.client = httpx.AsyncClient()

    @allure.step('Total Amount User Negative')
    @pytest.mark.asyncio
    async def total_amount_negative(self, headers, expected_status,uuid):
        response = await self.client.get(
            url = self.endpoints.total_amount(uuid),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
        
    @allure.step('Get Accounts Ewallet Negative')
    @pytest.mark.asyncio
    async def get_accounts_ewallet_negativ(self, headers, expected_status):
        response = await self.client.get(
            url = self.endpoints.get_accounts_ewallet,
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
    
    @allure.step('Get Ewallet Currencies Negative')
    @pytest.mark.asyncio
    async def get_ewallet_currencies(self, headers, expected_status):
        response = await self.client.get(
            url = self.endpoints.get_ewallet_currencies,
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)

    @allure.step('Get Entity Ewallets Negative')
    @pytest.mark.asyncio
    async def get_entity_ewallets(self, headers, expected_status, uuid):
        response = await self.client.get(
            url = self.endpoints.get_entity_ewallets(uuid),
            headers=headers
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)
    
    @allure.step('Create Entity Ewallet Negative')
    @pytest.mark.asyncio
    async def create_entity_ewallet(self,headers, expected_status, uuid):
        response = await self.client.post(
            url=self.endpoints.create_entity_ewallet,
            headers = headers,
            json = {"currency_id": uuid}
        )
        self.assert_bad_response(response, expected_status)
        self.attach_response_to_allure(response)

    async def close(self):
        await self.client.aclose()