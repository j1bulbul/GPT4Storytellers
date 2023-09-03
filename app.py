import os
from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

story_data = {
    "exposition": "",
    "risingAction": "",
    "climax": "",
    "fallingAction": "",
    "resolution": ""
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/interact', methods=['POST'])
def interact():
    section = request.json['section']
    message = request.json['message']

    # Update the story_data dictionary with the received data
    story_data[section] = message

    try:
        # Call to GPT-3 for summarization
        response=openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant/editor who is an expert in storytelling and/or screenwriting."},
                {"role": "user", "content": f"Summarize the following section of the plot: {message}"}
             ],
            temperature=0.25
            )
        summary = response.choices[0].message['content'].strip()

        # Printing the received data and the summary to the console (optional)
        print("Received section:", section)
        print("Received message:", message)
        print("Summary:", summary)

        # Return the summary in the response
        return jsonify({"response": summary})

    except Exception as e:
        # Print the error to the console
        print("Error with OpenAI API call:", str(e))
        # Return a generic error message to the user
        return jsonify({"response": "There was an error processing the request. Please try again."})

@app.route('/chat', methods=['POST'])
def chat():
    section = request.json['section']
    user_message = request.json['message']

    # Fetch the original text from the story_data dictionary
    original_text = story_data.get(section, "")

    try:
        # Call to GPT-3 for chat interaction
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant/editor who is an expert in storytelling and/or screenwriting and is not overly verbose unless necessary"},
                {"role": "user", "content": f"Discuss the following {section}: {original_text}"},
                {"role": "user", "content": user_message}
            ],
            temperature=0.25
        )
        chat_response = response.choices[0].message['content'].strip()

        # Return the chatbot response
        return jsonify({"response": chat_response})

    except Exception as e:
        # Print the error to the console
        print("Error with OpenAI API call:", str(e))
        # Return a generic error message to the user
        return jsonify({"response": "There was an error processing the request. Please try again."})

if __name__ == '__main__':
    app.run(debug=True)
