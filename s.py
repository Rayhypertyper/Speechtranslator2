import streamlit as st
from google.cloud import speech
from os import path
from scipy.io import wavfile
import time
from io import BytesIO
from pydub import AudioSegment
from googletrans import Translator
import os
from gtts import gTTS 
# import pyttsx3
import tempfile
import gtts.lang
 
# Header
st.header("English to Chinese Speech Translator")
dst = None

key_path = 'key.json'
if key_path:
    client = speech.SpeechClient.from_service_account_file(key_path)
else:
    st.error("API key not found")

file = st.audio_input("Record a voice message")
but = st.button('Upload audio')
if file is not None:
    pass
if but:
    file = st.file_uploader("Upload a file (Max: 10 MB and .wav file only)", type=['wav'])    

# Prevents the program from crashing when no file is uploaded
if file is not None:

    # Plays audio of what was recorded 
    # st.audio(file, format="audio/mpeg", loop=False)
    sise = file.size

    # Prevents file from exceeding 10MB because google won't allow it
    if sise > 10485760:
        st.error("File too large. Please select a file smaller than 10MB")
    else:
        st.success("File uploaded successfully")

    file = file.read()
    
    #Turns audio into text
    audio_file = speech.RecognitionAudio(content=file)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        language_code='en-US',
        use_enhanced=False,
        model="command_and_search"

    )

    response = client.recognize(
        config=config,
        audio=audio_file
    )
    st.write("Transcript:")

    # Prints text in english
    for result in response.results:
        text = result.alternatives[0].transcript
        st.write("{}".format(text))
        print(result.alternatives[0].transcript)
        
        # Translate text to chinese
        translator = Translator()
        b = translator.translate(text, dest='zh-CN')
        st.write("Translated transcript:")
        st.write("{}".format(b.text))
        
        # Speaks text in chinese
        t = b.text
        # engine = pyttsx3.init(driverName='espeak')
        # engine.setProperty('rate', 150)  # Speed of speech
        # engine.setProperty('voice', r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0")
        tts = gTTS(text=t, lang='zh-CN')
        # Creates temporary file to store audio
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            temp_filename = temp_file.name
            tts.save(temp_filename)
            # tts.save_to_file(t, temp_filename)
        # engine.runAndWait()
        st.write('Translated audio')
        st.audio(temp_filename, format="audio/wav")
        st.download_button('Download file', temp_filename, mime='audio/wav')
      

        boo = st.button("Reload")
        
        if boo:
            st.rerun()
            os.remove(temp_filename)
    #python -m streamlit run weatherweb.py
