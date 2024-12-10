import os
from linkedin_api import Linkedin

# Authenticate using any LinkedIn user account credentials in Notion/Important info
LINKEDIN_MAIL = os.environ['LINKEDIN_MAIL']
LINKEDIN_PASSWORD = os.environ['LINKEDIN_PASSWORD']
linkedin_api = Linkedin(LINKEDIN_MAIL, LINKEDIN_PASSWORD)

class LinkedinInfo:
    def __init__(self, linkedin_page_url: str):
        linkedin_username = linkedin_page_url.rstrip('/').split('/')[-1] # get the last segment of the URL
        self.data = linkedin_api.get_profile(linkedin_username)

    def get_summary(self):
        return self.data.get('summary')

    def get_headline(self):
        return self.data.get('headline')

    def get_experience(self):
        result = ""
        for el in self.data.get('experience'):
          result += f"{el['title']} at {el['companyName']} \n with this results {el['description']}"
        return result

    def get_volunteer(self):
        result = ""
        for el in self.data.get('volunteer'):
            result += f"{el['role']} at {el['companyName']} \n with this results {el['description']}"
        return result

    def get_projects(self):
        result = ""
        for el in self.data.get('projects '):
            result += f"{el['description']}"
        return result

def get_linkedin_profile_info(profile_url: str) -> str:
    profile = LinkedinInfo(profile_url)
    result = f"""
    Summary: {profile.get_summary()}
    Headline: {profile.get_headline()}
    Experience: {profile.get_experience()}
    """
    #     Volunteer: {profile.get_volunteer()}
    # Projects: {profile.get_projects()}
    return result

# GET a profile
# profile = LinkedinInfo("https://www.linkedin.com/in/sofiia-shaposhnikova/")