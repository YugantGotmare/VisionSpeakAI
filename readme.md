# VisionSpeakAI

VisionSpeakAI is an innovative application that combines real-time webcam video streaming with speech recognition and content description. Using this application, users can interact with the system through voice commands to describe the contents of the current video frame.

## Features

- Real-time webcam video streaming.
- Speech recognition to take user input.
- Content description using AI models.
- Voice feedback for user interactions.

## Requirements

- Python 3.7 or higher
- Tkinter
- opencv-python
- Pillow
- pyttsx3
- SpeechRecognition
- python-dotenv
- google-generativeai
- pyaudio

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/EyeSpeak-AI.git
    cd EyeSpeak-AI
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up Google Cloud API:
    - Create a project on Google Cloud Platform and enable the Speech-to-Text API.
    - Download the credentials JSON file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to this file.
    - Set up the Google Generative AI API and obtain the API key.

5. Create a `.env` file in the project directory and add your Google API key:
    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

Run the application:
```sh
python main.py
