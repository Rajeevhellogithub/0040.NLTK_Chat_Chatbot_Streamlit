import streamlit as st
from nltk.chat.util import Chat, reflections

pairs = [
    ["(.*)?my name is(.*)", ["Hello %2, how can I help you?"]],
    ["(.*)?help(.*)", ["How can I help you"]],
    ["(.*)?your name(.*)", ["My name is RoboChat"]],
    ["(.*)?how are you(.*)", ["I am doing very well!", "I am great!"]],
    ["(.*)?sorry(.*)", ["Its alright", "Its OK, never mind that"]],
    ["(.*)?(good|well|okay|ok)(.*)", ["Nice to hear that!", "Alright, great!"]],
    ["(.*)?(hi|hey|hello|hola|holla) (.*)", ["Hello!", "Hey there!"]],
    ["(.*)?want(.*)", ["Make me an offer I can not refuse"]],
    ["(.*)?created(.*)", ["Rajeev created me using Python NLTK library", "It is a top secret!"]],
    ["(.*)?(location|city)(.*)", ['Hyderabad, India',]],
    ["(.*)?raining in(.*)", ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain"]],
    ["(.*)?health(.*)", ["Health is very important, but I am a program, so I don't need to worry about my health"]],
    ["(.*)?(sports|game|sport)(.*)", ["I'm a very big fan of Cricket"]],
    ["(.*)?(cricketer|batsman)(.*)", ["Virat Kohli"]],
    ["quit", ["Bye for now. See you soon!", "It was nice talking to you. See you soon!"]],
    ["(.*)", ['I did not understand!']]
]

# Initialize the Chatbot
chatbot = Chat(pairs, reflections)

# Streamlit app title
st.title("NLTK Chatbot in Streamlit")

# To store the chat history in the session state
if "history" not in st.session_state:
    st.session_state.history = []

# Chat interface using st.chat_input()
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user's message to the history
    st.session_state.history.append({"role": "user", "content": user_input})
    
    # Generate the bot's response
    bot_response = chatbot.respond(user_input) or "I'm not sure how to respond to that."

    # Add bot's message to the history
    st.session_state.history.append({"role": "bot", "content": bot_response})

# Display chat history
for chat in st.session_state.history:
    if chat["role"] == "user":
        st.chat_message("user").write(chat["content"])
    else:
        st.chat_message("bot").write(chat["content"])