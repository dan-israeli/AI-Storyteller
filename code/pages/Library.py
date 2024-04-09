# imports
from streamlit_extras.switch_page_button import switch_page
from utils import send_email, validate_email, PROJECT_WORKING_DIR
import streamlit as st
from time import sleep
import os


# constants
EMPTY = ""
global CHOSEN_FILE

# homepage button
if st.button(":house:"):
    switch_page("Homepage")

title = "Welcome To Your Library! 📚"
subtitle = "Here is some of your best work:"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: left; color: black; font-family: Andika'>{title}</h2>
<p style='text-align: left; color: black; font-family: Andika; font-size: 22px'>{subtitle}</p>
<br>
""", unsafe_allow_html=True)

# read the saved stories
files_lst = os.listdir(f"{PROJECT_WORKING_DIR}/saved_stories")

col1, col2, col3, col4 = st.columns([0.7, 0.1, 0.1, 0.1])

# display the save stories titles
for file_name in files_lst:
    story_title = file_name[:-4]

    # display the entire story (move to ReadSavedFile page)
    if col1.button(f"{story_title}"):
        st.session_state["file_name"] = file_name
        st.session_state["read_saved_story"] = False
        switch_page("ReadSavedFile")

    # delete story from the library
    if col2.button(":x:", key=f"{file_name}_x"):
        os.remove(f"{PROJECT_WORKING_DIR}/saved_stories/{file_name}")
        switch_page("Library")

    # share the story
    if col3.button(":envelope_with_arrow:", key=f"{file_name}_share"):
        st.session_state["share_story"] = story_title

# share story
if st.session_state["share_story"] != EMPTY:
    user_email = st.text_input(label=f"Share '{st.session_state['share_story']}':", placeholder="Please enter the email you want to share with:")

    # send the story via email
    if user_email != EMPTY:

        # check email address is valid
        if validate_email(user_email):
            story = open(f"{PROJECT_WORKING_DIR}/saved_stories/{st.session_state['share_story']}.txt").read()
            send_email(st.session_state['share_story'], story, user_email)

            st.write("The story has been sent!")
            sleep(2)

            st.session_state['share_story'] = EMPTY
            switch_page("Library")

        # prompt the user to enter a valid email address
        else:
            st.write("Please enter an email address!")
