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
    def test_accounts_headers(self, headers, expected_status, get_currency_id, get_ewallet_id):
        self.accounts_api_negativ.total_amount_negativ(headers, expected_status,get_currency_id)
        self.accounts_api_negativ.get_accounts_ewallet_negativ(headers,expected_status)
        self.accounts_api_negativ.get_ewallet_currencies(headers, expected_status)
        self.accounts_api_negativ.get_entity_ewallets(headers,expected_status, get_ewallet_id)


    @pytest.mark.parametrize(
        ('uuid ,expected_status'), [
            ('invalid uuid', 404),
            ('12345', 404),
            ('00000000-0000-0000-0000-000000000000', 404),
        ]
    )
    def test_accounts_uuid(self, uuid, expected_status, headers = Headers.basic):
        self.accounts_api_negativ.total_amount_negativ(headers, expected_status,uuid)
        self.accounts_api_negativ.get_entity_ewallets(headers,expected_status, uuid)

    