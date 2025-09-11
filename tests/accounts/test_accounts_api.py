import allure
import pytest

@allure.epic('Test Services - Accounts')
class TestAccounts():

    @allure.title('Test GET /accounts/total-amount/{currency_id}')
    @pytest.mark.asyncio
    async def test_total_amount(self, get_currency_id, base):
        base.logger.get().info(
            f'Test launch - GET /accounts/total-amount/{get_currency_id}/, currency_id = {get_currency_id}'
        )
        await base.accounts_api.total_amount(get_currency_id)

    @allure.title('Test POST /accounts/ewallets{currency_id}')
    @pytest.mark.skip
    @pytest.mark.asyncio
    async def test_create_entity_ewallet(self, get_currency_id, base):
        base.logger.get().info(f'Test launch - POST /accounts/ewallets/{get_currency_id}/, currency_id = {get_currency_id}')
        await base.accounts_api.create_entity_ewallet(get_currency_id)

    @allure.title('Test GET /accounts/ewallets/')
    @pytest.mark.asyncio
    async def test_get_accounts_ewallet(self, base):
        base.logger.get().info('Test launch - GET /accounts/ewallets/')
        await base.accounts_api.get_accounts_ewallet()

    @allure.title('Test GET /accounts/ewallets/currencies')
    @pytest.mark.asyncio
    async def test_get_ewallet_currencies(self, base):
        base.logger.get().info('Test launch - GET /accounts/ewallets/currencies')
        await base.accounts_api.get_ewallet_currencies()
    
    @allure.title('Test GET /accounts/ewallets/{item_id}')
    @pytest.mark.asyncio
    async def test_get_entity_ewallets(self, get_ewallet_id, base):
        base.logger.get().info(f'Test launch - GET /accounts/ewallets/{get_ewallet_id}, item_id = {get_ewallet_id}')
        await base.accounts_api.get_entity_ewallets(get_ewallet_id)
 