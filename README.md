# Gian_Marco's_Chatbot
Chat Bot tailored to answer any question regarding Gian Marco Innocenti
This repository contains the source code and resources for a chatbot implemented using a Multi-Layer Perceptron (MLP) neural network. The chatbot is designed to understand and respond to user input, classifying it into predefined intents.

## Features
Intent Classification: The chatbot uses an MLP architecture to classify user input into predefined intents, allowing it to understand the user's purpose or query.

Natural Language Processing: The chatbot employs natural language processing techniques, including tokenization and lemmatization, to preprocess and understand user input.

Training Data: Training data for the chatbot is stored in a JSON file, containing intents, patterns, and responses. The model is trained on this data to learn patterns and associations.


## Deployment Locally

If you wish to tailor the chatbot to answaer specific questions about another topic follow the next steps:
- clone git hub repository
- create virtual environment using the requirements.txt file
- update the **intents.json** file and save the changes.
- run the **new.py** file to create a new model.
- **IMPORTANT** The new.py , intents.json , and Gian_Marco_Chatbot.py must all be in the same directory
- run the following comand in the terminal to launch the streamlit application to interact with the chatbot **streamlit run Gian_Marco_Chatbot.py** 
