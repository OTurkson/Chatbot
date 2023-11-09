# Import necessary libraries
import json # To load intents.json file
import spacy # To load the English language model
import random  # To randomly select a response
from os import system # To clear the console
from colorama import init, Fore, Style # To color the text
import time # To add a delay

init(autoreset=True) # reset color after use

def intro(): # Print the bot's intro
    system('cls')  # Clear the console
    print(Style.BRIGHT + Fore.BLUE +'''
                         /$$
                        | $$
      /$$$$$$   /$$$$$$$| $$
     /$$__  $$ /$$_____/| $$
    | $$$$$$$$| $$      | $$
    | $$_____/| $$      | $$
    |  $$$$$$$|  $$$$$$$| $$
     \_______/ \_______/|__/  
    ''' + Style.RESET_ALL +  Style.BRIGHT + Fore.WHITE +   '''                     
    \033[2;3;37m(Type 'quit' or 'exit' to terminate the program.)\033[0m                  
    ''')

    print(Style.BRIGHT + Fore.BLUE + "ECL: Hello! I'm ECL, your personal assistant. How can I help you today?")  # Print the bot's greeting

intro() # Print the bot's intro

# Load the English language model
nlp = spacy.load("en_core_web_sm") 

# Load data from intents.json file
with open('intents.json') as file:
    data = json.load(file)

intents = data['intents'] # Get the intents from the data

def get_response(input_text):
    doc = nlp(input_text)  # Process the input text with spaCy
    
    # Loop through the intents and find matching patterns
    for intent in intents:
        for pattern in intent['patterns']:
            pattern_doc = nlp(pattern)  # Process the pattern with spaCy
            if all(token.text.lower() in [t.text.lower() for t in doc] for token in pattern_doc):
                return random.choice(intent['responses'])  # Return a random response from the intent
    return "I'm not sure how to respond to that."  # Default response

# Main interaction loop
while True: 
    try:
        user_input = input(Style.BRIGHT  + "You: ").lower().replace("'","").replace("?","").replace("!","").replace(".","").replace("-","").strip()  # Prompt for user input
    except KeyboardInterrupt: # If user presses Ctrl+C, exit the program
        print(Style.BRIGHT + Fore.RED+"\nECL: Goodbye!")
        time.sleep(1)
        exit(system('cls'))  # Clear the console and exit the program
    if user_input == 'quit' or user_input=='exit':  # If user types 'quit' or 'exit', exit the program
        print(Style.BRIGHT + Fore.RED+"ECL: Goodbye!") # Print the bot's response.
        time.sleep(1)
        exit(system('cls'))  # Clear the console and exit the program
    elif user_input=="clear" or user_input=="cls":  # If user types 'clear', clear the console:
        intro() # Print the bot's intro
    elif user_input=="help":  # If user types 'help', print the help message
        print(Style.BRIGHT + Fore.BLUE+'''ECL: What do you need help working on?''')
    elif user_input == '': #empty input
        print(Style.BRIGHT + Fore.BLUE+"ECL: It seems you haven't provided any information. Anything you would like to say or know?") 
    else:
        response = get_response(user_input)  # Get a response based on the intent
        print(Style.BRIGHT + Fore.BLUE + f"ECL: {response}")  # Print the bot's response.