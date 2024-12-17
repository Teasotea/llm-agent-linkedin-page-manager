
import streamlit as st
from linkedin_llm_agent.idea_generation import get_ideas
from dotenv import load_dotenv
load_dotenv()
# App title
st.title("Generate Idea Page") 

profile_url = st.text_input("Linkedin Profile to analyze:")

# Run the function when the button is pressed
try:
    if st.button("Generate Ideas For Linkedin Profile"):

        st.write("Analyzing profile of", profile_url)
        strings = get_ideas(profile_url).split(';') # Call the function
    
    
        for num,string in enumerate(strings):
            # Create a container for each string
            with st.container():
                # Display the string in a box
                st.text_area(label = f'Idea #{num+1}',value=string, key=string)
    

except Exception as e:
    st.write(f"{e}")
    
            