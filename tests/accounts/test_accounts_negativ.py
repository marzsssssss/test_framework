import pytest

from config.base_test import BaseTest
from core.headers import Headers

class TestAccountsNegativ(BaseTest):


    @pytest.mark.parametrize(
        ('headers ,expected_status'), [
            (Headers.empty_token, 401),
            (Headers.invalid_token, 401),
            (Headers.missing_token, 401)
        ]
    )
    def test_accounts(self, headers, expected_status, get_currency_id, get_ewallet_id):
        self.accounts_api_negativ.total_amount_negativ(headers, expected_status,get_currency_id)
        self.accounts_api_negativ.get_accounts_ewallet_negativ(headers,expected_status)
        self.accounts_api_negativ.get_ewallet_currencies(headers, expected_status)
        self.accounts_api_negativ.get_entity_ewallets(headers,expected_status, get_ewallet_id)
    