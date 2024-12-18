import streamlit as st

generate_page = st.Page("streamlit-ui/generate_ideas.py", title="Generate ideas")
generate_post = st.Page("streamlit-ui/generate_post.py", title="Generate Post")

pg = st.navigation([generate_page, generate_post])
st.set_page_config(page_title="Agentify application")
pg.run()