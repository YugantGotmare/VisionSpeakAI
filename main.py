import tkinter as tk
from tkinter import ttk
import pyttsx3
from video_stream import VideoStreamHandler
from content_description import ContentDescriber

# Function to speak a welcome message
engine = pyttsx3.init()
welcome_message = "Welcome to the VisionSpeakAI application"
engine.say(welcome_message)
engine.runAndWait()

# Main GUI setup and button handlers
root = tk.Tk()
root.title("Webcam Stream")

# Style for ttk widgets
style = ttk.Style()
style.theme_use("clam")  # You can change the theme to your preference

# Welcome label
welcome_label = ttk.Label(root, text="Welcome to VisionSpeakAI", font=("Helvetica", 18))
welcome_label.pack(pady=10)

# Canvas for video stream
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Entry for user input
user_input = ttk.Entry(root, width=50, font=("Helvetica", 12))
user_input.pack(pady=10)

# Start video stream
video_handler = VideoStreamHandler(root, canvas)
content_describer = ContentDescriber(root, user_input, video_handler)
video_handler.start_stream()

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

describe_button = ttk.Button(button_frame, text="Speak", width=20, command=content_describer.threaded_describe_content)
describe_button.pack(side=tk.LEFT, padx=5)

button = ttk.Button(button_frame, text="Terminate", width=20, command=video_handler.stop_video)
button.pack(side=tk.LEFT, padx=5)

# Message label
message_label = ttk.Label(root, textvariable=content_describer.message_var, wraplength=500, font=("Helvetica", 12))
message_label.pack()

root.mainloop()
