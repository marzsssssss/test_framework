from config.base_test import BaseTest


class TestAccountsFlow(BaseTest):

    def test_entity_ewallet_get_post(self, get_currency_id):
        ewallet_id = self.accounts_api.create_entity_ewallet(get_currency_id)
        self.accounts_api.get_entity_ewallets(ewallet_id.id)
    
    def get_accounts(self, get_currency_id):
        self.accounts_api.total_amount(get_currency_id)
        self.accounts_api.get_accounts_ewallet()
        self.accounts_api.get_ewallet_currencies()