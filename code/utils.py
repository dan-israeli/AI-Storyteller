# imports
from email.mime.multipart import MIMEMultipart
from elevenlabs.client import ElevenLabs
from email.mime.text import MIMEText
from openai import OpenAI
import streamlit as st
import elevenlabs
import smtplib
import re


# constants
EMPTY = ""

voice_dict = {"Sarah": "EXAVITQu4vr4xnSDxMaL",
              "Arnold": "VR6AewLTigWG4xSOukaG",
              "Rachel": "21m00Tcm4TlvDq8ikWAM",
              "George": "JBFqnCBsd6RMkjVDRZzb",
              "Michael": "flq6f7yk4E4fJM5XTYuZ",
              "Dorothy": "ThT5KcBeYPX3keUQqHPh"}


# API keys
ELEVENLABS_API_KEY = 'Enter ElevenLabs API key here'
CHATGPT_API_KEY = 'Enter OpenAI API key here'

# email login credentials
SENDER_EMAIL = "projectiis857@gmail.com"
EMAIL_PASSWORD = 'Enter Email password (from the report) here'

# project working directory path
PROJECT_WORKING_DIR = r'Enter the path of the directory where the project files are located'


def story_init():
    """
    Initialize new story parameters.
    """

    st.session_state["location"] = EMPTY

    st.session_state["genre"] = EMPTY

    st.session_state["mc_name"] = "decided by you"

    st.session_state["user_criticism"] = EMPTY

    st.session_state["read_location"] = False

    st.session_state["messages_history"] = []

    st.session_state["num_sections_left"] = st.session_state["num_sections"]

    st.session_state["story_title"] = EMPTY

    st.session_state["current_section"] = EMPTY

    st.session_state["generate_current_section"] = True


def settings_init():
    """
    Initialize global settings.
    """

    if "voice" not in st.session_state:
        st.session_state["voice"] = ("Sarah", 0)

    if "num_sections" not in st.session_state:
        st.session_state["num_sections"] = 5

    if "voice_guidance" not in st.session_state:
        st.session_state["voice_guidance"] = False

    if "story_audio" not in st.session_state:
        st.session_state["story_audio"] = True

    if "settings_play_audio" not in st.session_state:
        st.session_state["settings_play_audio"] = [False, EMPTY]


def voice_guidance_init():
    """
    Initialize voice guidance boolean parameters (for each of the relevent pages).
    """

    st.session_state["voice_guidance_location"] = True

    st.session_state["voice_guidance_genre"] = True

    st.session_state["voice_guidance_mc_name"] = True

    st.session_state["voice_guidance_story_review"] = True

    st.session_state["voice_guidance_save_story"] = True

    st.session_state["voice_guidance_bad_story"] = True


def play_audio(text, voice_name, stability=0.5):
    """
    Gets a text and a speaker's voice, and plays an audio of the
    text being read by the speaker. The reading will be done according to the
    stability parameter.
    """
    # set API key
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # define voice
    voice_id = voice_dict[voice_name]
    voice = elevenlabs.Voice(
        voice_id=voice_id,
        settings=elevenlabs.VoiceSettings(
            stability=stability,
            similarity_boost=0.5
        )
    )

    # define audio object
    audio = client.generate(
        text=text,
        voice=voice,
        stream=True
    )

    # play the audio object using the streaming function
    elevenlabs.stream(audio)


def chatgpt(messages_history):
    """
    Get messages history of the conversation with the model, and return
    the model's response to it.
    """
    client = OpenAI(api_key=CHATGPT_API_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_history
    )

    return response.choices[0].message.content


def validate_email(email):
    """
    Gets an email address, and returns whether it is valid.
    """

    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True

    return False


def send_email(story_title, story, receiver_email):
    """
    Gets a story as well as its title, and sends it to the 'receiver_email' email address.
    """

    # define email information
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email

    message["Subject"] = f"You received a new story: {story_title}!"
    body = f"{story_title}\n\n{story}"
    message.attach(MIMEText(body, "plain"))

    # send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)

        server.send_message(message)
