import os
from dotenv import load_dotenv
from faker import Faker

fake = Faker()
load_dotenv()

class Headers():


    basic = {
        'Authorization': f"Bearer {os.getenv('ACCESS_TOKEN')}"
    }

    missing_toke = {}
    empty_token = {
        'Authorization': f"Bearer "
    }

    invalid_token = {
        'Authorization': f"Bearer {fake.pystr(min_chars=20, max_chars=40)}"
    }