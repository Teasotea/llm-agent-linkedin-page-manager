import streamlit as st

st.title("Welcome to LinkedIn post generator!")

# Create a text input field where the user can enter the post content
post_content = st.text_area("Enter your post content here:")
st.write("You entered:", post_content)

# Create a button that the user can click to generate the post
if st.button("Generate Post"):
    # Generate the post by adding some text to the user's input
    generated_post = f"🚀 {post_content} 🚀"
    st.write("Generated post:", generated_post)

# Create a button that the user can click to clear the input field
if st.button("Clear Input"):
    # Clear the input field by setting its value to an empty string
    post_content = ""
    st.write("Input cleared!")

# Create a button that the user can click to clear the generated post
if st.button("Clear Generated Post"):
    # Clear the generated post by setting its value to an empty string
    generated_post = ""
    st.write("Generated post cleared!")

# Create a button that the user can click to copy the generated post to the clipboard
if st.button("Copy Generated Post"):
    # Copy the generated post to the clipboard
    st.write("Generated post copied to clipboard!")
