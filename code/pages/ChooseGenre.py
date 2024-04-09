# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio
import streamlit as st

# constants
NAME = 0
EMPTY = ""


title = "Story's Genre"
subtitle = "Please choose a genre for your story:"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: left; color: black; font-family: Andika'>{title}</h2>
<p style='text-align: left; color: black; font-family: Andika; font-size: 22px'>{subtitle}</p>
""", unsafe_allow_html=True)

GENRES = ["Adventure", "Science Fiction", "Mystery", "Fantasy", "Fairy Tale", "Animals"]

# create a button for each genre
col0, col1, col2 = st.columns(3)
for i, genre in enumerate(GENRES):
    if i % 3 == 0:
        col = col0
    elif i % 3 == 1:
        col = col1
    else:
        col = col2

    # highlight (with red) the chosen genre
    if st.session_state["genre"] == genre:
        button_text = f":red[{genre}]"

    else:
        button_text = f":black[{genre}]"

    if col.button(button_text):
        st.session_state["genre"] = genre
        st.session_state["read_chosen_genre"] = True

        switch_page("ChooseGenre")

st.write("")

_, col1, col2, _ = st.columns([0.25, 0.25, 0.25, 0.25])

# previous button to the previous page (ChooseLocation)
if col1.button(":arrow_left:"):
    st.session_state["read_location"] = False
    switch_page("ChooseLocation")

# next button to the next page (ChooseName)
if col2.button(":arrow_right:"):
    # the user chose a genre, can proceed to ChooseName
    if st.session_state["genre"] != EMPTY:
        switch_page("ChooseName")

    # prompt the user to choose a genre
    else:
        st.write("Please choose a genre!")
        if st.session_state["voice_guidance"]:
            play_audio("Please choose a genre!", st.session_state["voice"][NAME], stability=0.8)


# voice guidance
if st.session_state["voice_guidance_genre"] and st.session_state["voice_guidance"]:
    text = "Please choose a genre for your story by clicking a button. When you are done, click the right arrow button at the bottom."
    st.session_state["voice_guidance_genre"] = False
    play_audio(text, st.session_state["voice"][NAME])

if st.session_state["read_chosen_genre"] and st.session_state["voice_guidance"]:
    st.session_state["read_chosen_genre"] = False
    play_audio(st.session_state["genre"], st.session_state["voice"][NAME], stability=1)
