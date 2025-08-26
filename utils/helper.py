import allure 
import json  
from allure_commons.types import AttachmentType

class Helper():

    def attach_respons(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name='API Response', attachment_type=AttachmentType.JSON)

    def assert_response(self, response):
        if response.status_code == 200:
            return response.ok, f"HTTP failed with status code {response.status_code} / {response.json()}"
        else:
            raise ValueError(f'Incorrect response object {response.status_code}/{response.json()}')
        
    