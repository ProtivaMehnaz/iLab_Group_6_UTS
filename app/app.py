import streamlit as st
import pandas as pd
from joblib import load




# -- Set page config
apptitle = 'DT2 & Obesity'

st.set_page_config(page_title=apptitle, page_icon="⚕️")

         
          
def page_home():
    st.write('36105 iLab: Capstone Project - Autumn 2024 - UTS')
    # Title
    st.title('How lifestyle/habits can lead to obesity and diabetes type 2')

def page_survey():
    st.title("Tell us about your lifestyle/habits")


def page_results():
    st.title("Know your status")


def main():
    st.sidebar.title("Explore")
 
    # Create links for each page
    page_links = {
        "Home": "Home",
        "Survey": "Survey",
        "Know Your Status": "Know Your Status"
    }

    # Display the selectbox in the sidebar
    selected_page = st.sidebar.selectbox("Go to", list(page_links.values()))

    # Check the selected page and execute the corresponding function
    if selected_page == "Home":
        page_home()

    elif selected_page == "Survey":
        page_survey()

    elif selected_page == "Know Your Status":
        page_results()



"""
    # Create links for each page
    # Create buttons with icons for each page
    button_home = st.sidebar.button("🏠 Home")
    button_survey = st.sidebar.button("📝 Survey")
    button_results = st.sidebar.button("📊 Know Your Status")

    # Check which button is clicked and execute the corresponding function
    if button_home:
        page_home()

    if button_survey:
        page_survey()

    if button_results:
        page_results()

"""

if __name__ == "__main__":
    main()

          
          




          
          