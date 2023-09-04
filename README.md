# StoryGPT: A Storytelling Assistant using OpenAI GPT-4

StoryGPT is a web application that leverages the OpenAI API to assist users in receiving feedback, brainstorm new ideas, or identify plot holes for their story.  Whether you're drafting a screenplay or brainstorming plot points, StoryGPT is here to act as a fresh set of "eyes" for your work.

## Features

- **Interactive Plot Point Selection**: Select different sections of your story (exposititon, rising action, climax, falling action, resolution), input text you have for this section fo your story (actual script/novel or outline), and receive a summary of that section in a flow chart for your reference.
- **Chat with GPT-3**: Interact directly with GPT-4, which is "aware" of the section in your story you are discussing and the actual content for that part in your story, in order to: receive feedback, brainstorm new plot ideas, or refine existing plot ideas.

![Plot Point Selection](INSERT_GIF_LINK_HERE "Plot Point Selection Demo")
![Chat with GPT-3](INSERT_GIF_LINK_HERE "Chat with GPT-3 Demo")

## How It Works

1. Select a section of the story you want to work on.
2. Input your existing story, text for that section from your outline, or even just initial thoughts/ideas.
3. Get a summary of that story section based on your provided text.
4. Interact in real-time with a context-aware chatbot powered by GPT-4 for a dynamic brainstorming and feedback session.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **API**: OpenAI API

## Installation & Usage

1. Clone this repository: `git clone https://github.com/j1bulbul/StoryGPT/tree/main`.
2. Navigate to the project directory and install the required packages: `pip install -r requirements.txt`.
3. **(Optional)** Setup a virtual environment and activate it.
4. **(Optional)** Connect to the OpenAI API by storing your OpenAI secret key in a `.env` file.
5. Run the Flask server: `python app.py`.
6. Open your browser and navigate to `http://localhost:5000`, or whichever port you have manually set to host the server, to start using StoryGPT.

## Future Enhancements

- **Plot Hole Detection Mode**: Toggle a decicated plot hole detection mode within chatbot to analyse new plot additions you may have for plot holes or inconsistencies (or just analyse your existing story content for plot holes)
- **Character Development Mode**: Toggle a character development mode within chatbot geared towards discussing characters with GPT-4 and getting feedback on your character backstories, motivations, and arcs
- **Character List**: Obtain a list of all characters appearing in your story, a short description of each, and a list of interactions they have with other characters
- **Script or Novel Toggle**: Provide a toggle switch between script or novel prior to pasting in story text.
  - If script is selected: the flow-chart showcasing story outline will be an auto-generated beatsheet (with GPT summarised text for each beat)
  - If novel is selected: typical five act structure as shown in GIF above

## License

This project is licensed under the MIT License.
