from config.base_test import BaseTest

class TestAccouts(BaseTest):

    def test_account_ewallet(self, get_currency_id):
        self.accounts_api.total_amount(get_currency_id)