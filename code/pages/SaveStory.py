# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio, chatgpt, PROJECT_WORKING_DIR
from time import sleep
import streamlit as st

# constants
NAME = 0


txt1 = "I'm so glad you enjoyed it!"
txt2 = "Would you like to add it to your library?"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<p style='text-align: center; color: black; font-family: Andika; font-size: 32px'>{txt1}</p>
<p style='text-align: center; color: black; font-family: Andika; font-size: 28px'>{txt2}</p>
<br>
""", unsafe_allow_html=True)


_, col1, col2, _ = st.columns([0.29, 0.25, 0.25, 0.21])

# save story to library button
if col1.button("Save :books:"):
    prompt = f"""Please write the entire story in one piece, according to the choices I made."""
    st.session_state["messages_history"].append({"role": "user", "content": prompt})

    full_story = chatgpt(st.session_state["messages_history"])

    with open(f"{PROJECT_WORKING_DIR}/saved_stories/{st.session_state['story_title']}.txt", "w") as f:
        f.write(full_story)

    txt = "Your story has been saved!"
    st.markdown(f"""
    <head>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
    </style>
    </head>

    <p style='text-align: center; color: black; font-family: Andika; font-size: 20px'>{txt}</p>
    """, unsafe_allow_html=True)
    sleep(1)
    switch_page("Homepage")

# homepage button
if col2.button("No Thanks!"):
    sleep(0.5)
    switch_page("Homepage")

# voice guidance
if st.session_state["voice_guidance_save_story"] and st.session_state["voice_guidance"]:
    text = "I'm so glad you enjoyed it! if you would like to add it to your library, click the button on the left."
    st.session_state["voice_guidance_save_story"] = False
    play_audio(text, st.session_state["voice"][NAME])
