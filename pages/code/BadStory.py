# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio, story_init
import streamlit as st

# constants
NAME = 0
EMPTY = ""


title1 = "I'm so sorry that you didn't like the story."
title2 = "Tell me, what's wrong?"
text = "Please write your opinion in order to help me rewrite the story to your liking:"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<p style='text-align: center; color: black; font-family: Andika; font-size: 32px'>{title1}</p>
<p style='text-align: center; color: black; font-family: Andika; font-size: 30px'>{title2}</p>
<br>
<p style='text-align: left; color: black; font-family: Andika; font-size: 17px'>{text}</p>
""", unsafe_allow_html=True)


st.session_state["user_criticism"] = st.text_input("a", label_visibility="collapsed",
                                                   placeholder="Please write your opinion here:")

st.write("")

text = "You can always leave this text box empty, to be able to create a completely new story!"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<p style='text-align: left; color: red; font-family: Andika; font-size: 17px'>{text}</p>
<br><br>
""", unsafe_allow_html=True)


_, col1, col2, _ = st.columns([0.3, 0.25, 0.25, 0.2])

# homepage button
if col1.button(":house:"):
    switch_page("Homepage")

# submit button
if col2.button("Submit"):

    # if the user didn't submit any criticism, start creating a new story (move to ChooseLocation page)
    if st.session_state["user_criticism"] == EMPTY:
        story_init()
        switch_page("ChooseLocation")

    # create the fix prompt based on the user criticism
    else:
        fix_prompt = f"""
        I have the following criticism about the story that you wrote:
        "{st.session_state["user_criticism"]}"
        Can you regenerate the same story, while fixing it according to the criticism above?
        The location, genre, main character name and number of sections should be the same as last time.
        """
        st.session_state["messages_history"].append({"role": "user", "content": fix_prompt})

        st.session_state["num_sections_left"] = st.session_state["num_sections"]

        st.session_state["generate_current_section"] = True

        switch_page("Story")

# voice guidance
if st.session_state["voice_guidance_bad_story"] and st.session_state["voice_guidance"]:
    text = """I'm so sorry that you didn't like the story. Please submit your opinion in order for me to rewrite
            the story to your liking. You can always skip this step, to be able to create a completely new story."""
    st.session_state["voice_guidance_bad_story"] = False
    play_audio(text, st.session_state["voice"][NAME])
