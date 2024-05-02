from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

genai.configure(api_key='AIzaSyAhCLD7xS06LV2pSkKMEEo_uLE1K3wbDuE')
model = genai.GenerativeModel('gemini-1.0-pro-latest')

def serve_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    disease = data.get('disease', '')
    medication = data.get('medication', '')
    surgery = data.get('surgery', '')
    misc = data.get('misc', '')
    name = 'Sameer Suleman'
    # Construct prompt based on user input
    prompt = f'''My name is {name}, I am a fictional character, I currently have the disease {disease}, and I am currently taking 
                 the following medication(s): {medication}, I have had a previous surgery for {surgery} and there is more I need you to know: 
                 {misc}. Given what I have told you, I want you to generate a theoretical calendar for me in NA timezone, considering my current 
                 situation and needs. I want this calendar to be best suited for me to take the right medicine and do my physiotherapy exercises. 
                 Avoid assigning tasks during regular working hours 9-5 on weekdays, as I embark on the road to recovery, do so by returning this as 
                 the text you would see in a .ics file. Avoid scheduling tasks from 9am to 5pm on weekdays.'''

    # Generate content using GEMINI AI model
    response = model.generate_content(prompt)

    # Check if response contains a valid Part
    if response and response.result and response.result.candidates:
        candidate = response.result.candidates[0]  # Assuming you want the first candidate
        if candidate.safety_ratings:
            # Check if the response was not blocked
            if not any(r.blocked for r in candidate.safety_ratings):
                return jsonify({'response': candidate.text})

    # If response is invalid or blocked, return an error message
    return jsonify({'error': 'Failed to generate valid response from the model'})

if __name__ == '__main__':
    app.run(debug=True, port=5174)
