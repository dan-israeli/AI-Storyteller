# imports
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
from utils import play_audio, PROJECT_WORKING_DIR

# constants
NAME = 0


file_name = st.session_state["file_name"]

# get story file
file_path = f"{PROJECT_WORKING_DIR}/saved_stories/{file_name}"

# read saved story button
if st.button(":loudspeaker:", help="Click here for me to read the story!"):
    st.session_state["read_saved_story"] = True

title = file_name[:-4]

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>
<h2 style='text-align: center; color: black; font-family: Andika'>{title}</h2>
""", unsafe_allow_html=True)

# display the entire story
with open(file_path, 'r') as f:
    st.session_state["saved_story_text"] = f.read()
    st.write(st.session_state["saved_story_text"])

    st.session_state["write_saved_story"] = False

st.write("")

col1, col2 = st.columns([0.45, 0.55])

# library button
if col2.button(":books:"):
    switch_page("Library")

# read the story button
if st.session_state["read_saved_story"]:
    st.session_state["read_saved_story"] = False
    play_audio(st.session_state["saved_story_text"], st.session_state["voice"][NAME])
