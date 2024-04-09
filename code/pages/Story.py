# imports
from streamlit_extras.switch_page_button import switch_page
from utils import play_audio, chatgpt
from time import sleep
import streamlit as st

# constants
NAME = 0
EMPTY = ""

# stop story button
if st.button(":hand:", help="You can always stop the story by clicking here!"):
    sleep(0.5)
    switch_page("BadStory")

if len(st.session_state["messages_history"]) == 0:

    # if the user didn't select the main character name, generate it
    if st.session_state["mc_name"] == "decided by you":
        name_prompt = """Give me a first name of main character in a children's book."""
        st.session_state["mc_name"] = chatgpt([{"role": "user", "content": name_prompt}])

    # generate the story's title
    title_prompt = f"""I have an idea for a children's book. 
    The main charatcer's name is {st.session_state["mc_name"]},
    I want it to take place in {st.session_state["location"]}, 
    and the genre is {st.session_state["genre"]}.
    Please suggest me a very generic title for the story, based on this information only.
    """

    st.session_state["story_title"] = chatgpt([{"role": "user", "content": title_prompt}]).replace('"', '')

    # initial prompt
    prompt = f"""
    Hey, I want you to write an interesting children's story, with a plot twist and a climax.
    I want it to take place in {st.session_state["location"]},
    the genre should be {st.session_state["genre"]},
    and the main character's name is {st.session_state["mc_name"]}.
    At key points in the story, you should prompt me to choose between two possible actions to determine the direction of the plot.
    The two possible actions should be written in different lines. Before the first possible action, write "Option 1:".
    Before the second possible action, write "Option 2:".
    When I choose the possible action that I want, the plot should continue according to my choice. Moreover, I do not want you to generate the entire story in 
    advance, I want you to generate each section separately, and wait for my choice before you continue to the next section.
    I want the story to contain {st.session_state["num_sections"]} sections in total.
    """

    st.session_state["messages_history"].append({"role": "user", "content": prompt})


st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: center; color: black; font-family: Andika'>{st.session_state["story_title"]}</h2>
<br>
""", unsafe_allow_html=True)

# generate current section
if st.session_state["generate_current_section"]:
    current_section = chatgpt(st.session_state["messages_history"])
    st.session_state["messages_history"].append({"role": "assistant", "content": current_section})

    st.write(current_section)
    st.session_state["current_section"] = current_section
    st.session_state['num_sections_left'] -= 1
    st.session_state["generate_current_section"] = False
    st.session_state["read_current_section"] = True

st.write("")

# if story didn't end
if st.session_state['num_sections_left'] != 0:
    _, col1, col2, col3 = st.columns([0.3, 0.25, 0.35, 0.1])

    # number of story sections left remainder
    if st.session_state['num_sections_left'] > 1:
        reminder = f"I remind you that you need to end the story in {st.session_state['num_sections_left']} sections."
    else:
        reminder = "I remind you to finish the story in your following answer."

    # option 1 button
    if col1.button("Option 1"):
        st.session_state["messages_history"].append(
            {"role": "user", "content": f"""Option 1. {reminder}"""})

        st.session_state["generate_current_section"] = True
        switch_page("Story")

    # option 2 button
    if col2.button("Option 2"):
        st.session_state["messages_history"].append(
            {"role": "user", "content": f"""Option 2. {reminder}"""})

        st.session_state["generate_current_section"] = True
        switch_page("Story")

    # regenerate current section button
    if col3.button(":arrows_counterclockwise:", help="Click here to regenerate this section!"):
        regen_options_prompt = """
        I don't like this section, please rewrite it. Make sure that the options you provide are different from the
        options in the section I didn't like."""

        st.session_state["messages_history"].append(
            {"role": "user", "content": regen_options_prompt})

        st.session_state["generate_current_section"] = True
        st.session_state['num_sections_left'] += 1

        switch_page("Story")

# story ended
else:
    col1, col2 = st.columns([0.45, 0.55])
    if col2.button("Done"):
        switch_page("StoryReview")

# read current section
if st.session_state["read_current_section"] and st.session_state["story_audio"]:
    play_audio(st.session_state["current_section"], st.session_state["voice"][NAME])
    st.session_state["read_current_section"] = False
