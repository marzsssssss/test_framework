from services.accounts.accounts_api import AccountsAPI

class BaseTest:

    # Пока что сделаем просто запуск автотеста по total_amount, рефрешить токен будет через фикстуру
    # На будушее в setup_method можно добавить регистрацию или авторизацию
    def setup_method(self):
        self.accounts_api = AccountsAPI()