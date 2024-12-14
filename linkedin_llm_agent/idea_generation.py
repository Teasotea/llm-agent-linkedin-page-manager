from tools.call_llm import *
from prompts import *
from tools.get_linkedin_profile_info import *
PROFILE_URL = "https://www.linkedin.com/in/sofiia-shaposhnikova/"


def get_ideas():
    link_profile_info = get_linkedin_profile_info(PROFILE_URL)
    profile_features = call_llm(extracting_key_features_from_link_info.format(link_profile_info))
    
    system_prompt = system_prompt_for_onbording.format(profile_features,link_profile_info)
    prompt = idea_generation_prompt
    res = call_llm(prompt=prompt,system_promt=system_prompt)
    return res

if __name__ == '__main__':
    print(get_ideas())

