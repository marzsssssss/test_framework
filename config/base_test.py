import pytest

from services.accounts.accounts_api import AccountsAPI
from services.accounts.accounts_api_negative import AccountsNegativeAPI
from services.admin_entities.admin_entities_api import AdminEntitiesAPI
from services.admin_entities.admin_entities_api_negative import AdminEntitiesNegative
from core.logger import Logger

class BaseTest:

    def __init__(self):
        self.logger = Logger('Base Test')
        self.accounts_api = AccountsAPI()
        self.accounts_api_negative = AccountsNegativeAPI()
        self.admin_entities_api = AdminEntitiesAPI()
        self.admin_entities_api_negative = AdminEntitiesNegative()