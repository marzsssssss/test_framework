import allure

from config.base_test import BaseTest

@allure.epic('Test Services - Admin Entities')
class TestAdminEntites(BaseTest):

    @allure.title('Test GET /accounts/total-amount/{currency_id}')
    def test_get_entites_account_list(self):
        self.admin_entities_api.logger.info(f'Test launch - GET /admin/entities/accounts/unovay_name ')
        self.admin_entities_api.get_entities_accounts_list()

    def test_post_accouts_adjust_balance(self,get_ewallet_id):
        self.admin_entities_api.logger.info('Test launch - POST /admin/entities/accounts/adjust-balance/')
        self.admin_entities_api.post_entities_accouts_adjust_balance(get_ewallet_id)