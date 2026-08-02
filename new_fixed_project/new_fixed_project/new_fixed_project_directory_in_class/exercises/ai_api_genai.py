from google import genai
import api_key

API_KEY = api_key.API_KEY

client = genai.Client(api_key=API_KEY)

# prompt = "tell me a joke about cats?"
# response = client.models.generate_content(
#   #  model="gemini-2.5-flash" ,
#  #   contents=prompt
# )
#print(response)
#print(response.text)


def run_generate_contents(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

prompt = "tell me a joke about cats?"
joke = run_generate_contents(prompt)
print(joke)


