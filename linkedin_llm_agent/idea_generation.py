from tools.call_llm import *
from prompts import *
from tools.get_linkedin_profile_info import *

PROFILE_URL = "https://www.linkedin.com/in/sofiia-shaposhnikova/"



def get_ideas(profile_url:str)->str:
    '''
    Generate post ideas for specific linkedin profile based on info from this profile.
    A
    rgs:
        profile_url (str): url for linkedin_page

    Returns:
        str: The list of ideas for linkedin posts.
    '''
    link_profile_info = get_linkedin_profile_info(profile_url)
    profile_features = call_llm(extracting_key_features_from_link_info.format(link_profile_info))
    
    system_prompt = system_prompt_for_onbording.format(profile_features,link_profile_info)
    prompt = idea_generation_prompt
    res = call_llm(prompt=prompt,system_promt=system_prompt)
    return res

