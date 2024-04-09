# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio
import streamlit as st

# constants
NAME, IDX = 0, 1
TO_READ, TEXT = 0, 1
EMPTY = ""

VOICE2IDX = {'Sarah': 0,
             'Arnold': 1,
             'Rachel': 2,
             'George': 3,
             'Michael': 4,
             'Dorothy': 5}

# homepage button
if st.button(":house:"):
    switch_page("Homepage")

title = "General Settings"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: left; color: black; font-family: Andika'>{title}</h2>
<br>
<br>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 4, 4])
col1.write("")

# choose speaker
col1.write('Speaker:')
col1.write("")
cur_speaker = col2.selectbox('Speaker:',
                             options=['Sarah', 'Arnold', 'Rachel', 'George', 'Michael', 'Dorothy'],
                             index=st.session_state["voice"][IDX],
                             label_visibility="collapsed")

if cur_speaker != st.session_state["voice"][NAME]:
    st.session_state["voice"] = (cur_speaker, VOICE2IDX[cur_speaker])

    st.session_state["settings_play_audio"] = [True, f"Hello, my name is {cur_speaker}."]
    switch_page("Settings")

st.write("")

# choose number of story sections
col1.write("Number of Story Sections:")
col1.write("")
col2.write("")
st.session_state["num_sections"] = col2.select_slider("Number of Story Sections:",
                                options=[3, 4, 5, 6, 7],
                                value=st.session_state["num_sections"],
                                label_visibility="collapsed")

st.write("")

# toggle story audio
col1.write("Story Audio:")
col1.write("")
col2.write("")
story_audio = col2.toggle("story audio", value=st.session_state["story_audio"], label_visibility="collapsed")

if story_audio != st.session_state["story_audio"]:
    st.session_state["story_audio"] = story_audio

    if story_audio:
        text = "Story audio on."
    else:
        text = "Story audio off."

    st.session_state["settings_play_audio"] = [True, text]
    switch_page("Settings")


# toggle voice guidance
col1.write("Voice Guidance:")
col1.write("")
col2.write("")
voice_guidance = col2.toggle("", value=st.session_state["voice_guidance"],
                             help="Voice guidance will read instructions when needed, and buttons' content when clicked.")

if voice_guidance != st.session_state["voice_guidance"]:
    st.session_state["voice_guidance"] = voice_guidance

    if voice_guidance:
        text = "Voice guidance on."

    else:
        text = "Voice guidance off."

    st.session_state["settings_play_audio"] = [True, text]
    switch_page("Settings")


# custom voice button
if st.button("Wanna choose a custom voice? Click here!"):
    switch_page("CustomVoice")

if st.session_state["settings_play_audio"][TO_READ]:
    st.session_state["settings_play_audio"][TO_READ] = False
    play_audio(st.session_state["settings_play_audio"][TEXT], voice_name=st.session_state["voice"][NAME], stability=1)

