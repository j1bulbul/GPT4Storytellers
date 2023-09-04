import os
from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.DEBUG)

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
    logging.debug(f"Interact Endpoint - Received section: {section}")
    logging.debug(f"Interact Endpoint - Received message: {message}")
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
    content_type = request.json['contentType']
    chat_mode = request.json['chatMode']
    logging.debug(f"Chat Endpoint - Current story section: {section}")
    logging.debug(f"Chat Endpoint - User message: {user_message}")
    logging.debug(f"Chat Endpoint - Selected content type: {content_type}")
    logging.debug(f"Chat Endpoint - Selected chat mode: {chat_mode}")
    # Fetch the original text from the story_data dictionary
    original_text = story_data.get(section, "")
    story_context = f"Here's the content for the {section}: {original_text}"
    if chat_mode == "general":
        system_prompt = "You are a helpful assistant who is a storytelling expert."
    elif chat_mode == "plothole":
        system_prompt = "You are a storytelling expert specialized in identifying plotholes and inconsistencies."
    elif chat_mode == "character":
        system_prompt = "You are a storytelling expert with a focus on character development."
    elif chat_mode == "brainstorm":
        system_prompt = "You are a brainstorming assistant with an expertise in storytelling."

    if content_type == "outline":
        initial_prompt = "This is an outline of a story."
    else:
        initial_prompt = "This is a story."

    if chat_mode == "general":
        initial_prompt += f"Provide general feedback/discuss the {content_type} with user."
    elif chat_mode == "plothole":
        initial_prompt = f"Analyze the provided {content_type} and identify any plotholes or inconsistencies. List them in a numerical format (e.g., '1. Background Inconsistency', '2. Motivation Inconsistency') with a brief explanation for each. Additionally, if the user presents new plot ideas, evaluate them for inconsistencies and use the same numerical list format in your answer."
    elif chat_mode == "character":
        initial_prompt += "Discuss the characters and their development/character arcs."
    elif chat_mode == "brainstorm":
        initial_prompt += f"Help the user brainstorm content tailored to the specific section of the {content_type}, whether it's exposition, rising action, climax, falling action, or resolution."

    try:
        # Call to GPT-3 for chat interaction
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": story_context},
                {"role": "user", "content": initial_prompt},
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
