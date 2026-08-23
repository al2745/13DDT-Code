from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv() #load environmental variables from os.environ, reads .env file

#store anthropic api in 'client' after getting it from the computer operating sys
client = Anthropic(
  api_key = os.getenv("DDT_API_KEY")
)

def analyse_article(prompt, token_amount):
    message = client.messages.create(
        model = "claude-haiku-4-5-20251001", #claude sonnet model, avoiding fable because of obscurity
        max_tokens = token_amount, #tokens the AI uses to respond, lesser tokens = reduce need to purchase restore tokens (newly added slider)
        messages = [
        {
        "role": "user", #AI knows prompt is from user
        "content": prompt #AI reads this as initial content
        }
    ]
    )

    print(message.content) #fixed claude from returning thinkingblock instead of textblock

    response = "No response received" #returns this as default if claude does not return any text
    for block in message.content: #set up loop
        if hasattr(block, "text"): #does current text block have "text" attribute? yes = true, no = false
            response = str(block.text) #store text from claude as "response"
            break #response found = stop loop
    return response #return to main program