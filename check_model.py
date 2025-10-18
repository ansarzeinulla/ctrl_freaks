import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load your API key
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Available models:")
for m in genai.list_models():
  # Check if the model supports the 'generateContent' method
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)