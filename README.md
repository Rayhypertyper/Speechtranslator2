# Speech Translator

This project is a Streamlit application that translates English speech to Chinese text and provides audio output of the translated text. It uses Google Cloud Speech-to-Text API for speech recognition and Google Translate API for translation.

## Features

- Record audio from the microphone
- Convert speech to text using Google Cloud Speech-to-Text API
- Translate text from English to Chinese using Google Translate API
- Convert translated text to speech using gTTS (Google Text-to-Speech)
- Play the translated audio and provide a download option

## Requirements

- Python 3.7 or higher
- Streamlit
- Google Cloud Speech
- Scipy
- Pydub
- Googletrans
- Python-dotenv
- gTTS
- SpeechRecognition

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Rayhypertyper/speech.git
    cd speech
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Install the required system packages:

    Create a [packages.txt](http://_vscodecontentref_/0) file with the following content:

    ```plaintext
    espeak
    ffmpeg
    libespeak1
    libespeak-dev
    ```

    Then, install the packages listed in [packages.txt](http://_vscodecontentref_/1):

    ```sh
    sudo apt-get update
    sudo apt-get install -y $(cat packages.txt)
    ```

## Usage

1. Set up your Google Cloud credentials:

    - Create a service account in the Google Cloud Console and download the JSON key file.
    - Save the key file as [key.json](http://_vscodecontentref_/2) in the project directory.
    - Create a [.env](http://_vscodecontentref_/3) file in the project directory with the following content:

    ```plaintext
    GOOGLE_APPLICATION_CREDENTIALS=key.json
    ```

2. Run the Streamlit application:

    ```sh
    streamlit run s.py
    ```

3. Open your web browser and go to `http://localhost:8501` to use the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.