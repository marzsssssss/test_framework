import allure
import pytest
import os
from faker import Faker

from config.base_test import BaseTest
from core.headers import Headers
from payloads.admin_entities_payloads import Payloads

fake = Faker()

@allure.feature('Test Services - Admin Entities - Negative')
class TestAdminEntitiesNegative(BaseTest):

    name = os.getenv('UN_NAME')
    json = lambda ewallet_id: Payloads.adjust_balance(ewallet_id)

    @allure.title('Negative Tests Accounts Headers')
    @pytest.mark.parametrize(
        ('headers', 'expected_status', 'name'), [
            (Headers.empty_token, 401, name),
            (Headers.invalid_token, 401, name),
            (Headers.missing_token, 401, name)
        ]
    )
    def test_admin_entities_headers(self, headers, expected_status, name, get_ewallet_id):
        json = Payloads.adjust_balance(get_ewallet_id)
        self.admin_entities_api_negative.logger.info(f'Test launch Negative Headers  - GET - /admin/entities/accounts/ Negative, headers -  {headers} - expected status - {expected_status}')
        self.admin_entities_api_negative.get_entities_accounts(name, headers, expected_status)
        self.admin_entities_api_negative.logger.info(f'Test launch Negative Headers  - POST - /admin/entities/accounts/adjust-balance Negative, headers -  {headers} - expected status - {expected_status}')
        self.admin_entities_api_negative.post_entities_accounts_adjust(json, headers, expected_status)

        
    @allure.title('Test GET /admin/entities/accounts/unovay_name Negative')
    @pytest.mark.parametrize(
        ('name','expected_status'), [
            (fake.random_number(digits=16), 404),
            ('', 404)
        ]
    )
    def test_admin_get_entities(self, name, expected_status, headers = Headers.basic):
        self.admin_entities_api_negative.logger.info(f'Test launch Negative name  - GET /admin/entities/accounts/unovay_name, expected status - {expected_status}')
        self.admin_entities_api_negative.get_entities_accounts(name, headers, expected_status)


    @allure.title('Test POST - Missing Required Fields')
    @pytest.mark.parametrize(
        'field', [
            'invoice_direction',
            'account_ewallet_id',
            'amount',
            'hidden'
        ]
    )
    def test_missing_required_fields(self, field, get_ewallet_id, headers=Headers.basic):
        json_required = Payloads().without_field(field, get_ewallet_id)
        expected_status = 204 if field == 'hidden' else 422
        self.admin_entities_api_negative.logger.info(
            f'Test launch Missing Required Field - POST, field: {field}, expected_status: {expected_status}'
        )
        self.admin_entities_api_negative.post_entities_accounts_adjust(json_required, headers, expected_status)


    @allure.title('Test POST - Invalid Field Values')
    @pytest.mark.parametrize(
        'field', [
            'invoice_direction',
            'account_ewallet_id',
            'amount',
            'hidden'
        ]
    )
    def test_invalid_field_values(self, field, get_ewallet_id, headers=Headers.basic):
        payload_keys = Payloads().field_test(field, get_ewallet_id)
        for payload in payload_keys:
            self.admin_entities_api_negative.logger.info(
                f'Test launch Invalid Field Value - POST, field: {field}, payload: {payload}'
            )
            self.admin_entities_api_negative.post_entities_accounts_adjust(payload, headers, expected_status=422)   