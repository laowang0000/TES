import streamlit as st

# Input
name = st.text_input("Enter your name")

# Output
if name:
    st.write(name, "output")
else:
    st.write("Please enter your name")
