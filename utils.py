import os

from openai import OpenAI
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')
client = OpenAI( api_key=OPENAI_API_KEY)

# def generate_gift_ideas(description, api_key):
#     try:
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=description,
#             max_tokens=150,
#             api_key=api_key
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
def generate_gift_ideas(description, api_key):
    try:
        response = client.completions.create(
        prompt=description,
        max_tokens=150,
        model='davinci-002')
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
