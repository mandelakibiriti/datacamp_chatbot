import re

# Define variables
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

#Define a dictionary of intents (keywords) entities (responses)
keywords = {
    'goodbye': ['bye', 'farewell'], 
    'thankyou': ['thank', 'thx'], 
    'greet': ['hello', 'hi', 'hey']
    }

responses = {
    'goodbye': ['bye', 'farewell'], 
    'thankyou': ['thank', 'thx'], 
    'greet': ['hello', 'hi', 'hey']
}

# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, entities in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(entities))
    
# Print the patterns
# print(patterns)

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message 
        if pattern.search(message):
            matched_intent = intent
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thanks very much!")