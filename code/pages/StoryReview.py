# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio
import streamlit as st

# constants
NAME = 0


title = "Wow! That was such an amazing story!"
subtitle = "Did you enjoy it as well?"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<p style='text-align: center; color: black; font-family: Andika; font-size: 32px'>{title}</p>
<p style='text-align: center; color: black; font-family: Andika; font-size: 28px'>{subtitle}</p>
<br>
""", unsafe_allow_html=True)

_, col1, col2, _ = st.columns([0.32, 0.24, 0.24, 0.2])

# save story button
if col1.button("Yes! :heavy_check_mark:"):
    switch_page("SaveStory")

# bad story button
if col2.button("No. :x:"):
    switch_page("BadStory")

# voice guidance
if st.session_state["voice_guidance_story_review"] and st.session_state["voice_guidance"]:
    text = "Wow! That was such an amazing story! Did you enjoy it as well?"
    st.session_state["voice_guidance_story_review"] = False
    play_audio(text, st.session_state["voice"][NAME])


