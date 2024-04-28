import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAhCLD7xS06LV2pSkKMEEo_uLE1K3wbDuE')

model = genai.GenerativeModel('gemini-1.0-pro-latest')



name = 'Sameer Suleman'
response = model.generate_content(f"If my name is {name} return both my first name and lastname backwards")
print(response.text)


# to send data into json what I was thinking of was receiving and assigning a bunch of values into new variables,
# then throwing that into a json template which we will then put into json/xml file which we can then use to update the website? lol