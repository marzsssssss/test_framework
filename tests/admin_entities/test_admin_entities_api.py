import allure
import os
import pytest

from config.base_test import BaseTest

@allure.epic('Test Services - Admin Entities')
@pytest.mark.adminentities
class TestAdminEntites(BaseTest):

    @allure.title('Test  GET /admin/entities/accounts/un_name')
    def test_get_entites_account_list(self):
        self.admin_entities_api.logger.info(f'Test launch - GET /admin/entities/accounts/un_name')
        self.admin_entities_api.get_entities_accounts_list(os.getenv('UN_NAME'))

    @allure.title('Test POST /admin/entities/accounts/adjust-balance/')
    def test_post_accouts_adjust_balance(self,get_ewallet_id):
        self.admin_entities_api.logger.info('Test launch - POST /admin/entities/accounts/adjust-balance/')
        self.admin_entities_api.post_entities_accouts_adjust_balance(get_ewallet_id)