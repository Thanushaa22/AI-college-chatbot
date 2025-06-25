import openai
from flask_cors import CORS
CORS(app)


openai.api_key = "your-api-key"

def get_response(user_input):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )
    return completion.choices[0].text.strip()
