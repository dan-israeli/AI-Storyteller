# imports
from streamlit_extras.switch_page_button import switch_page
import streamlit as st


title = "Create Custom Voice"

text1 = """
        Please prepare a recording of your custom voice (up to 5 minutes).<br>
        To cover a wide range of pronunciations, it is recommended to read the following sentences: <br>"""
text2 = """
        1. As I speak, my words ripple outward, creating a symphony of sound that dances in the air. <br><br>
        2.Each syllable I utter weaves together to form a tapestry of sound, echoing the essence of my being. <br><br>
        3. In the silence, my voice emerges, a beacon of expression guiding the way through the labyrinth of existence. <br><br>
        4. My voice is a river, flowing with the currents of emotion and meaning, carving its path through the landscape of sound. <br><br>
        5. With each breath, I release my voice into the world, a melody that harmonizes with the rhythm of life. <br><br>
        6. Words are the threads of my voice, weaving a tapestry of communication that connects souls across space and time. <br><br>
        7. In the stillness of the moment, my voice resonates, filling the void with the cadence of my thoughts and feelings. <br><br>
        8. Like a painter with a brush, I craft my voice into strokes of expression, painting the canvas of sound with shades of meaning. <br><br>
        9. My voice is a reflection of my innermost self, echoing the depths of my soul with every utterance. <br><br>
        10. Through the vibrations of sound, I imprint my essence onto the fabric of reality, leaving echoes of my presence in the world. <br>"""
text3 = """
        When you are done, please upload your file below. <br>
        We will send you an email when you're custom voice is ready to use!<br><br>
        * Only send voice recordings of people who agree to record their voice."""


st.markdown(f"""
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Bubblegum+Sans&family=Mystery+Quest&display=swap')
</style>
</head>

<h2 style='text-align: left; color: black; font-family: Andika'>{title} </h2>
<p style='text-align: left; color: black; font-family: Andika; font-size: 16px'>{text1}</p>
<p style='text-align: left; color: black; font-family: arial; font-size: 14px'>{text2}</p>
<p style='text-align: left; color: black; font-family: Andika; font-size: 16px'>{text3}</p>

<br>
""", unsafe_allow_html=True)

st.file_uploader("Upload your recording here (.mp3 format)")

st.write("")

# settings button
if st.button(":arrow_left:"):
    switch_page("Settings")
