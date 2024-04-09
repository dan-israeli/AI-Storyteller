# imports
from utils import story_init, settings_init, voice_guidance_init
from streamlit_extras.switch_page_button import switch_page
import streamlit as st

# constants
EMPTY = ""


settings_init()

col1, col2 = st.columns([0.08, 1])

# settings button
if col1.button(":gear:"):
    switch_page("Settings")

# library button
if col2.button(":books:"):
    st.session_state["share_story"] = EMPTY
    switch_page("Library")

title = "What Story Would You Like To Hear Today?"
subtitle = "Let's create your new favorite story, together!"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<p style='text-align: center; color: black; font-family: Mystery Quest; font-size: 50px' >{title}</p>
<p style='text-align: center; color: black; font-family: Andika; font-size: 30px'>{subtitle}</p>
<br>
<br>
<br>
""", unsafe_allow_html=True)


col1, col2 = st.columns([3.5, 5])

# start creating a story button (move to ChooseLocation page)
if col2.button("Get Started!"):
    story_init()
    voice_guidance_init()
    switch_page("ChooseLocation")
