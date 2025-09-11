import allure
import pytest
import os
from faker import Faker

from core.headers import Headers
from payloads.admin_entities_payloads import Payloads

fake = Faker()

@allure.feature('Test Services - Admin Entities - Negative')
class TestAdminEntitiesNegative():

    @pytest.mark.asyncio
    @allure.title('Negative Tests Accounts Headers')
    @pytest.mark.parametrize(
        ('headers', 'expected_status'), [
            (Headers.invalid_token, 401),
            (Headers.missing_token, 401)
        ]
    )
    async def test_admin_entities_headers(self, headers, expected_status, base, get_ewallet_id):
        json = Payloads.adjust_balance(get_ewallet_id)
        name = os.getenv('UN_NAME')
        base.logger.get().info(f'Test launch Negative Headers  - GET - /admin/entities/accounts/ Negative, headers -  {headers} - expected status - {expected_status}')
        await base.admin_entities_api_negative.get_entities_accounts(name, headers, expected_status)
        base.logger.get().info(f'Test launch Negative Headers  - POST - /admin/entities/accounts/adjust-balance Negative, headers -  {headers} - expected status - {expected_status}')
        await base.admin_entities_api_negative.post_entities_accounts_adjust(json, headers, expected_status)

        
    @pytest.mark.asyncio
    @allure.title('Test GET /admin/entities/accounts/unovay_name Negative')
    @pytest.mark.parametrize(
        ('name','expected_status'), [
            (fake.random_number(digits=16), 404),
            ('', 404)
        ]
    )
    async def test_admin_get_entities(self, name, expected_status, base, headers = Headers.basic):
        base.logger.get().info(f'Test launch Negative name  - GET /admin/entities/accounts/unovay_name, expected status - {expected_status}')
        await base.admin_entities_api_negative.get_entities_accounts(name, headers, expected_status)


    @pytest.mark.asyncio
    @allure.title('Test POST - Missing Required Fields')
    @pytest.mark.parametrize(
        'field', [
            'invoice_direction',
            'account_ewallet_id',
            'amount',
            'hidden'
        ]
    )
    async def test_missing_required_fields(self, field, get_ewallet_id, base, headers=Headers.basic):
        json_required = Payloads().without_field(field, get_ewallet_id)
        expected_status = 204 if field == 'hidden' else 422
        base.logger.get().info(
            f'Test launch Missing Required Field - POST, field: {field}, expected_status: {expected_status}'
        )
        await base.admin_entities_api_negative.post_entities_accounts_adjust(json_required, headers, expected_status)


    @pytest.mark.asyncio
    @allure.title('Test POST - /admin/entities/accounts/adjust-balance - Invalid invoice_direction')
    @pytest.mark.parametrize(
        ('invoice_direction', 'expected_status'), [
            ({"invoice_direction": fake.pystr(min_chars=4, max_chars=4)}, 422),
            ({"invoice_direction": fake.random_number(digits=3)}, 422),
            ({"invoice_direction": ""}, 422),
        ]
    )
    async def test_invalid_invoice_values(self, invoice_direction, expected_status, base, get_ewallet_id, headers=Headers.basic):
        base_payload = Payloads.adjust_balance(get_ewallet_id)
        payload = {**base_payload, **invoice_direction}
        base.logger.get().info(
            f'Test POST - /admin/entities/accounts/adjust-balance - Invalid invoice_direction, expected_status: {expected_status}, invoice_direction - {invoice_direction}'
        )
        await base.admin_entities_api_negative.post_entities_accounts_adjust(payload, headers, expected_status)



    @pytest.mark.asyncio
    @allure.title('Test POST - /admin/entities/accounts/adjust-balance - Invalid account_ewallet_id')
    @pytest.mark.parametrize(
        ('account_ewallet_id', 'expected_status'), [
            ({"account_ewallet_id": fake.random_number(digits=3)}, 422),
            ({"account_ewallet_id": fake.boolean()}, 422),
            ({"account_ewallet_id": fake.uuid4()}, 404),
            ({"account_ewallet_id": ""}, 422)
        ]
    )
    async def test_invalid_account_values(self, account_ewallet_id, expected_status, base, get_ewallet_id, headers=Headers.basic):
        base_payload = Payloads.adjust_balance(get_ewallet_id)
        payload = {**base_payload, **account_ewallet_id}
        base.logger.get().info(
            f'Test POST - /admin/entities/accounts/adjust-balance - Invalid account_ewallet_id, expected_status: {expected_status}, account_ewallet_id - {account_ewallet_id}'
        )
        await base.admin_entities_api_negative.post_entities_accounts_adjust(payload, headers, expected_status)

    
    @pytest.mark.asyncio
    @allure.title('Test POST - /admin/entities/accounts/adjust-balance - Invalid amount')
    @pytest.mark.parametrize(
        ('amount', 'expected_status'), [
            ({"amount": -10}, 422),
            ({"amount": 'ten'}, 422),
            ({"amount": 0}, 422),
            ({"amount": fake.boolean()}, 422)
        ]
    )
    async def test_invalid_amount_values(self, amount, expected_status, base, get_ewallet_id, headers=Headers.basic):
        base_payload = Payloads.adjust_balance(get_ewallet_id)
        payload = {**base_payload, **amount}
        base.logger.get().info(
            f'Test POST - /admin/entities/accounts/adjust-balance - Invalid amount, expected_status: {expected_status}, account_ewallet_id - {amount}'
        )
        await base.admin_entities_api_negative.post_entities_accounts_adjust(payload, headers, expected_status)


    @pytest.mark.asyncio
    @allure.title('Test POST - /admin/entities/accounts/adjust-balance - Invalid hidden')
    @pytest.mark.parametrize(
        ('hidden', 'expected_status'), [
            ({"hidden": "ten"}, 422),
            ({"hidden": fake.uuid4()}, 422),
            ({"hidden": 123}, 422),
        ]
    )
    async def test_invalid_hidden_values(self, hidden, expected_status, base, get_ewallet_id, headers=Headers.basic):
        base_payload = Payloads.adjust_balance(get_ewallet_id)
        payload = {**base_payload, **hidden}
        base.logger.get().info(
            f'Test POST - /admin/entities/accounts/adjust-balance - Invalid hidden, expected_status: {expected_status}, account_ewallet_id - {hidden}'
        )
        await base.admin_entities_api_negative.post_entities_accounts_adjust(payload, headers, expected_status)