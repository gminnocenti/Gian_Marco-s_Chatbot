import random
import json
import pickle
import numpy as np
import nltk
import streamlit as st
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
import streamlit as st
import streamlit.components.v1 as components

nltk.download('punkt')
nltk.download('wordnet')



lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')



def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words (sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class (sentence):
    bow = bag_of_words (sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes [r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice (i['responses'])
            break
    return result



st.title("Gian Marco's Chatbot")

# Introduction text
intro_text = """
👋 **Welcome to Gian's Chatbot!**
I'm your virtual assistant here to make your experience seamless. Whether you have questions, need assistance, or just want to chat, I'm here 24/7. Feel free to ask me anything!\n
🤖 **What I Can Help With:**
- Provide information on Gian Marco's Interests, Credentials, and Skills.
- Answer frequently asked questions.
- Assist with troubleshooting.
- Engage in friendly conversation!\n
🌐 **Navigation Tips:**
- Type your questions or commands in the chatbox.
- Explore various topics using keywords.\n
🔒 **Privacy Assurance:**
Your privacy is important. I don't store personal information, and our conversation is secure.
Now, how can I assist you today? Type your message below! ⬇️
"""

# Display the introduction text
st.markdown(intro_text, unsafe_allow_html=True)
session_state = st.session_state
st.divider()

if not hasattr(session_state, "conversation_history"):
    session_state.conversation_history = []

# Display the conversation history in the sidebar
for item in session_state.conversation_history:
    st.text(item)

# Recommended questions in a dropdown
recommended_questions = [
        "What is Gian Marco's work experience?",
    "What is Gian Marco's gpa or school average?",
        "major role in applaudo",
    "How can i get in contact with Gian Marco?","what are gian marco's passions or interests",
    "what are gian marcos' computational skills","list of important coursework"

    # Add more questions as needed
]

# User chooses either a recommended question or enters a custom question
user_choice = st.radio("Choose an option:", ["Select a Recommended Question", "Enter Custom Question"])

if user_choice == "Select a Recommended Question":
    selected_question = st.selectbox("Select a Recommended Question", recommended_questions)
    if selected_question:
        # Assuming you have defined predict_class and get_response functions
        ints = predict_class(selected_question)
        res = get_response(ints, intents)
        session_state.conversation_history.append(f"You: {selected_question}\nBot: {res}")
        st.write("Bot: "+ res)

elif user_choice == "Enter Custom Question":
    # Text input for custom questions
    user_input = st.text_input("Enter Custom Text:")
    if user_input:
        ints = predict_class(user_input)
        res = get_response(ints, intents)
        session_state.conversation_history.append(f"You: {user_input}\nBot: {res}")
        st.write("Bot: "+ res)
