from nltk.chat.util import Chat, reflections
import re

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

print("You can start chatting with the bot! Type 'quit' to exit.")

chat = Chat(pairs, reflections)
chat.converse()