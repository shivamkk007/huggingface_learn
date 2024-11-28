import gradio as gr
import requests
import io
from PIL import Image
import requests

#access tocken for the model
API_URL = "https://api-inference.huggingface.co/models/sd-community/sdxl-flash"
headers = {"Authorization": ""}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# function to generate image
def generate_picture(prompt):
	image_bytes = query({"inputs": prompt})
	image = Image.open(io.BytesIO(image_bytes))
	return image

# Gradio interface
trial =gr.Interface(fn=generate_picture,inputs="text", outputs="image")

trial.launch(share=True)
