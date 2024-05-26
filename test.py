# import threading
# import cv2
# from PIL import Image
# import io
# from dotenv import load_dotenv
# import os
# import tkinter as tk
# import pyttsx3
# import speech_recognition as sr
# import google.generativeai as genai
# import google.ai.generativelanguage as glm

# load_dotenv()
# genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
# model = genai.GenerativeModel('gemini-pro-vision')
# recognizer = sr.Recognizer()

# class ContentDescriber:
#     def __init__(self, root, user_input, video_handler):
#         self.root = root
#         self.user_input = user_input
#         self.video_handler = video_handler
#         self.message_var = tk.StringVar()
#         self.tts_engine = pyttsx3.init()
#         self.recognizer = sr.Recognizer()
#         self.microphone = sr.Microphone()

#     def describe_content(self):
#         current_frame = self.video_handler.get_current_frame()
#         if current_frame is not None:
#             pil_image = Image.fromarray(cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB))
#             img_byte_arr = io.BytesIO()
#             pil_image.save(img_byte_arr, format='JPEG')
#             # Process the image and generate description
#             description = "Description of the current frame"  # Placeholder for actual description
#             # Update the message variable with the description
#             self.message_var.set(description)
#             # Speak the description
#             self.tts_engine.say(description)
#             self.tts_engine.runAndWait()
#         else:
#             message = "No frame available"
#             self.message_var.set(message)
#             self.tts_engine.say(message)
#             self.tts_engine.runAndWait()

#     def threaded_describe_content(self):
#         describe_thread = threading.Thread(target=self.describe_content)
#         describe_thread.start()

#     def update_message(self, new_text):
#         current_text = self.message_var.get()
#         updated_text = current_text + new_text + "\n"
#         self.message_var.set(updated_text)

#     def listen_for_input(self):
#         with self.microphone as source:
#             while True:  # Continuous listening
#                 # print("Listening for user input...")
#                 # try:
#                 #     audio = self.recognizer.listen(source, timeout=1)  # Adjust timeout as needed
#                 #     print("Recognizing speech...")
#                 #     user_input_text = self.recognizer.recognize_google(audio)
#                 #     print(f"Recognized: {user_input_text}")
#                 #     self.user_input.set(user_input_text)
#                 # except sr.WaitTimeoutError:
#                 #     print("Listening timeout")
#                 # except sr.UnknownValueError:
#                 #     print("Could not understand audio")
#                 # except sr.RequestError as e:
#                 #     print(f"Error requesting speech recognition results: {e}")
#                 print("Speak something...")
#                 recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#                 audio_data = recognizer.listen(source)  # Listen for the audio input
                
#                 try:
#                     # Recognize the speech
#                     text = self.recognizer.recognize_google(audio_data)
#                     print("You said:", text)
#                     # Set the captured voice input to the user input entry
#                     self.root.after(0, self.user_input.insert, "end", text)
#                     # Automatically describe the frame after capturing voice input
#                     self.describe_content()
#                     break  # Exit the loop after capturing and processing the input
#                 except sr.UnknownValueError:
#                     print("Sorry, I could not understand what you said.")
#                 except sr.RequestError as e:
#                     print("Sorry, I could not request results from Google Speech Recognition service; {0}".format(e))

#     def threaded_listen_for_input(self):
#         listen_thread = threading.Thread(target=self.listen_for_input)
#         listen_thread.start()
