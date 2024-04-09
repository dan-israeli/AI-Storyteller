# imports
from streamlit_extras.switch_page_button import switch_page
from st_click_detector import click_detector
from utils import play_audio
import streamlit as st

# constants
NAME = 0
EMPTY = ""


title = "Story's Location"
subtitle = "Please choose a location for your story:"

st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: left; color: black; font-family: Andika'>{title}</h2>
<p style='text-align: left; color: black; font-family: Andika; font-size: 22px'>{subtitle}</p>
""", unsafe_allow_html=True)


LOCATIONS = [
    ("enchanted forest", 'https://drive.google.com/thumbnail?id=1hrkEIKKxDtpwF_VSfxpGo4H02bFRHjz3'),
    ("pirate island", 'https://drive.google.com/thumbnail?id=1d208gFslJVrgQyQg6445FZz654mrQi6N'),
    ("faraway kingdom", 'https://drive.google.com/thumbnail?id=1da8_wF2J0tUsL8ySn_dll9S49r6UXuys'),
    ("thrilling ocean", 'https://drive.google.com/thumbnail?id=1w3TM9DjSWafrAS2Eb7jJFEjJPGPG7Rax'),
    ("north pole", 'https://drive.google.com/thumbnail?id=1V4tJz9bxoN1tcgf-JrruCkhlow-m2liq'),
    ("outer space", 'https://drive.google.com/thumbnail?id=1agMo8xlIaG7vQIqkvIrRsbt2pVwZmTdt'),
    ("wild west", 'https://drive.google.com/thumbnail?id=1_NSWemCjsIms-JqMQidDqSILGM4baxDl'),
    ("haunted castle", 'https://drive.google.com/thumbnail?id=1Q-_z1V3qR7tq1lMxhReWzHFGfFri3ylN'),
    ("magical school", 'https://drive.google.com/thumbnail?id=1Ulws3s9sHUOnj0LxqiAB-R-uQrUauoRo')
    ]

# display the locations (clickable) images
content = "<br>"
for i, (loc, link) in enumerate(LOCATIONS):
    border_style = '2px solid black'

    # highlight (with red boarder) the chosen location
    if loc == st.session_state["location"]:
        border_style = '4px solid red'

    cur_content = f"""
        <a href='#' id='{loc}'><img width='28%' style='border:{border_style}' src='{link}'></a> &nbsp &nbsp
        """

    # 3 images per line
    if i == 3 or i == 6:
        content += '<br><br>'

    content += cur_content

# get the id of the selected location (image)
location = click_detector(content)

_, col1, col2, _ = st.columns([0.3, 0.2, 0.2, 0.3])

if col1.button(":house:"):
    switch_page("Homepage")

# next button to the next page (ChooseGenre)
if col2.button(":arrow_right:"):

    # the user chose a genre, can proceed to ChooseName
    if st.session_state["location"] != EMPTY:
        st.session_state["read_chosen_genre"] = False
        switch_page("ChooseGenre")

    # prompt the user to choose a location
    else:
        st.write("Please choose a location!")
        if st.session_state["voice_guidance"]:
            play_audio("Please choose a location!", st.session_state["voice"][NAME], stability=0.8)

# read the selected location if 'voice guidance' setting is on
if st.session_state["voice_guidance"] and st.session_state["read_location"]:
    play_audio(st.session_state["location"], st.session_state["voice"][NAME], stability=1)
    st.session_state["read_location"] = False

# update selected location
if location:
    refresh = st.session_state["location"] != location
    st.session_state["location"] = location

    # refresh the page if the previous chosen location is different from the current select one
    if refresh:
        st.session_state["read_location"] = True
        switch_page("ChooseLocation")

    # read the selected location if the user toggled the 'voice guidance' setting
    elif st.session_state["voice_guidance"]:
        play_audio(st.session_state["location"], st.session_state["voice"][NAME])


# voice guidance
if st.session_state["voice_guidance_location"] and st.session_state["voice_guidance"]:
    text = "Please choose a location for your story by clicking an image. When you are done, click the right arrow button at the bottom."
    st.session_state["voice_guidance_location"] = False
    play_audio(text, st.session_state["voice"][NAME])
