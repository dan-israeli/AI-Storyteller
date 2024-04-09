# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio
import streamlit as st

# constants
NAME = 0
EMPTY = ""


title = "Main Character's Name"
subtitle = "Please choose a name for your main character:"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: left; color: black; font-family: Andika'>{title}</h2>
<p style='text-align: left; color: black; font-family: Andika; font-size: 22px'>{subtitle}</p>

""", unsafe_allow_html=True)

# get the main character name
st.session_state["mc_name"] = st.text_input("a", label_visibility="collapsed",
                                            placeholder="Get ready to cheer for the amazing hero:")

text = "Not sure? You can always click on the right arrow, and I will choose a name for you!"
st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<p style='text-align: left; color: black; font-family: Andika; font-size: 15px'>{text} </p>
<br>
""", unsafe_allow_html=True)

_, col1, col2, _ = st.columns([0.25, 0.25, 0.25, 0.25])

# previous button to the previous page (ChooseGenre)
if col1.button(":arrow_left:"):
    if st.session_state["mc_name"] == EMPTY:
        st.session_state["mc_name"] = "decided by you"

    switch_page("ChooseGenre")

# next button to the next page (Story)
if col2.button(":arrow_right:"):
    if st.session_state["mc_name"] == EMPTY:
        st.session_state["mc_name"] = "decided by you"

    switch_page("Story")


# voice guidance
if st.session_state["voice_guidance_mc_name"] and st.session_state["voice_guidance"]:
    text = "Please choose a name for your main character. You can always click the right arrow, and I will choose it for you!"
    st.session_state["voice_guidance_mc_name"] = False
    play_audio(text, st.session_state["voice"][NAME])
