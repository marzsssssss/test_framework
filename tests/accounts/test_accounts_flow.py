import allure
import pytest

@allure.feature('Test Services - Accounts - Flow')
class TestAccountsFlow():

    @allure.title('Test Flow POST ewallet and get this ewallet')
    @pytest.mark.asyncio
    async def test_entity_ewallet_get_post(self, get_currency_id, base):
        base.logger.get().info(f'Flow - POST /accounts/ewallets/{get_currency_id}')
        ewallet_id = await base.accounts_api.create_entity_ewallet(get_currency_id)
        base.logger.get().info(f'Flow - and GET /accounts/ewallets/{ewallet_id.id}')
        await base.accounts_api.get_entity_ewallets(ewallet_id.id)
    
    @allure.title('3 GET - accounts/total-amount, accounts/ewallets, accounts/currencies')
    @pytest.mark.asyncio
    async def test_get_accounts(self, get_currency_id, base):
        base.logger.get().info(f'Test launch - GET /accounts/total-amount/{get_currency_id}/, currency_id = {get_currency_id}')
        await base.accounts_api.total_amount(get_currency_id)
        base.logger.get().info('Test launch - GET /accounts/ewallets/')
        await base.accounts_api.get_accounts_ewallet()
        base.logger.get().info('Test launch - GET /accounts/ewallets/currencies')
        await base.accounts_api.get_ewallet_currencies()