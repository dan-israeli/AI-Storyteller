# AI-Storyteller :robot: :book:

In our project, we created an interactive AI system which generates personalized and interactional children stories, as well as narrates them to the user.

## Running Instructions

First, download the files in the 'code' directory, and locate all of them in the same directory on your machine.

### Modifying the 'utils.py' File

Make the following changes in the 'utils.py' file:

Insert the **full path** of the project's current working directory (the directory where all the code files are located):

![image](https://github.com/cohen-ariel/AI-Storyteller/assets/127883151/c9834082-8fb0-4f59-9450-baff399eaa0c)

Insert the Email password specified in the Project Report (in the System Description section):

![image](https://github.com/cohen-ariel/AI-Storyteller/assets/127883151/e63f0e4f-3fa1-434d-8df5-c02053461c8b)

Insert your API keys for OpenAI and ElevenLabs in the designated area:

![image](https://github.com/cohen-ariel/AI-Storyteller/assets/127883151/d77a41a0-5853-4a1b-bc9d-aa7c42b68616)

*Create API key for OpenAI: https://openai.com/blog/openai-api

**Create API key for ElevenLabs (free): https://elevenlabs.io/api

### Installing Required Text-to-Speech Files

Download the files required for the Text-to-Speech model, in the following [link](https://technionmail-my.sharepoint.com/:u:/g/personal/dan_israeli_campus_technion_ac_il/EU0JTC-cmElHt6akxXAbRgEBGL-nuoqJHmIWkSezF32nrQ?e=if0j6j).

Watch the video [here](https://technionmail-my.sharepoint.com/:v:/g/personal/ariel_cohen_campus_technion_ac_il/EUJ1UGfEfEBKsI6uO1MzEmkBKyRDRyFwc-IRDEW8Zs2IEA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=67sIUf) for installation instructions.

### Creating Conda Environment

In the Anaconda Prompt, use the following command to create a conda environment from the 'ai_storyteller_env.yml' file provided in the project:
```bash
conda env create -f ai_storyteller_env.yml
```

Then, simply run the project using the following command:
```bash
streamlit run <PROJECT_WORKING_DIR>/Homepage.py
```
