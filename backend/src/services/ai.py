import google.genai as genai

client = genai.Client(api_key="AIzaSyDERgEMU7DomcTHPewBt2KigkO6hBwioxM")

def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
    )
    return response.text
