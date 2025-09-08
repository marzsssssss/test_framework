import allure
import pytest
import os

from config.base_test import BaseTest
from core.headers import Headers
from payloads.admin_entities_payloads import Payloads
@allure.feature('Test Services - Admin Entities - Negative')
class TestAdminEntitiesNegative(BaseTest):

    name = os.getenv('UN_NAME')
    json = lambda ewallet_id: Payloads.adjust_balance(ewallet_id)

    allure.title('Negative Tests Accounts Headers')
    @pytest.mark.parametrize(
        ('headers', 'expected_status', 'name'), [
            (Headers.empty_token, 401, name),
            (Headers.invalid_token, 401, name),
            (Headers.missing_token, 401, name)
        ]
    )

    def test_admin_entities_headers(self, headers, expected_status, name, get_ewallet_id):
        json = Payloads.adjust_balance(get_ewallet_id)
        self.admin_entities_api_negative.logger.info(f'Test launch Negative Headers  - GET - /admin/entities/accounts/, headers -  {headers} - expected status - {expected_status}')
        self.admin_entities_api_negative.get_entities_accounts(name, headers, expected_status)
        self.admin_entities_api_negative.logger.info(f'Test launch Negative Headers  - POST- /admin/entities/accounts/adjust-balance Negative, headers -  {headers} - expected status - {expected_status}')
        self.admin_entities_api_negative.post_entities_accounts_adjust(json, headers, expected_status)