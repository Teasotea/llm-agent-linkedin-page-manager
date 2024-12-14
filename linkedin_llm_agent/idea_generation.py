from tools.call_llm import *
from prompts import *
from tools.get_linkedin_profile_info import *




def get_ideas(profile_url:str)->str:
    """
    Generates a list of LinkedIn post ideas tailored to the specified LinkedIn profile.  
    This function analyzes the information available on the profile to create relevant and engaging post suggestions.

    Args:  
        profile_url (str): The URL of the LinkedIn profile to analyze.

    Returns:  
        str: A list of LinkedIn post ideas personalized for the profile.
    """

    link_profile_info = get_linkedin_profile_info(profile_url)
    profile_features = call_llm(get_key_features_from_user_info_prompt.format(link_profile_info))
    
    system_prompt = system_onboarding_prompt.format(profile_features,link_profile_info)
    prompt = idea_generation_prompt
    res = call_llm(prompt=prompt,system_promt=system_prompt)
    return res

