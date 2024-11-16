from linkedin_api import Linkedin
import json
import os

# Authenticate using any Linkedin user account credentials
GMAIL = os.environ['LINKEDIN_MAIL']
PASSWORD= os.environ['LINKEDIN_PASSWORD']
api = Linkedin(GMAIL,PASSWORD)

# GET a profile
profile = api.get_profile('sofiia-shaposhnikova')


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(profile, f, ensure_ascii=False, indent=4)