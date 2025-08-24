import allure 
import json  
from allure_commons.types import AttachmentType

class Helper():

    def attach_respons(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name='API Response', attachment_type=AttachmentType.JSON)

    def assert_response(self, response):
        if hasattr(response, 'ok'):
            return response.ok, f"HTTP failed with status code {response.status_code}"
        else:
            raise ValueError('Incorrect response object')
        
    