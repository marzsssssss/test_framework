from config.base_test import BaseTest


class TestAccountsFlow(BaseTest):

    def test_entity_ewallet_get_post(self, get_currency_id):
        self.accounts_api.logger.info(f'Flow - POST /accounts/ewallets/{get_currency_id}')
        ewallet_id = self.accounts_api.create_entity_ewallet(get_currency_id)
        self.accounts_api.logger.info(f'Flow - and GET /accounts/ewallets/{ewallet_id.id}')
        self.accounts_api.get_entity_ewallets(ewallet_id.id)
    
    def test_get_accounts(self, get_currency_id):
        self.accounts_api.logger.info(f'Test launch - GET /accounts/total-amount/{get_currency_id}/, currency_id = {get_currency_id}')
        self.accounts_api.total_amount(get_currency_id)
        self.accounts_api.logger.info('Test launch - GET /accounts/ewallets/')
        self.accounts_api.get_accounts_ewallet()
        self.accounts_api.logger.info('Test launch - GET /accounts/ewallets/currencies')
        self.accounts_api.get_ewallet_currencies()