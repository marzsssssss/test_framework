from config.base_test import BaseTest

class TestAccouts(BaseTest):

    def test_total_amount(self, get_currency_id):
        self.accounts_api.logger.info(f'Test launch - GET /accounts/total-amount/{get_currency_id}/, currency_id = {get_currency_id}')
        self.accounts_api.total_amount(get_currency_id)

    def test_create_entity_ewallet(self, get_currency_id):
        self.accounts_api.logger.info(f'Test launch - POST /accounts/ewallets/{get_currency_id}/, currency_id = {get_currency_id}')
        self.accounts_api.create_entity_ewallet(get_currency_id)

    def test_get_accounts_ewallet(self):
        self.accounts_api.logger.info('Test launch - GET /accounts/ewallets/')
        self.accounts_api.get_accounts_ewallet()

    def test_get_ewallet_currencies(self):
        self.accounts_api.logger.info('Test launch - GET /accounts/ewallets/currencies')
        self.accounts_api.get_ewallet_currencies()
    
    def test_get_entity_ewallets(self,get_ewallet_id):
        self.accounts_api.logger.info(f'Test launch - GET /accounts/ewallets/{get_ewallet_id}, item_id = {get_ewallet_id}')
        self.accounts_api.get_entity_ewallets(get_ewallet_id)
 