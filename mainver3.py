from tkinter import *
import customtkinter as ctk
from anthropic import Anthropic
import time
import requests
import os
from dotenv import load_dotenv
import sqlite3
#importing all external modules that will be needed for the program


load_dotenv()
#load environmental variables from os.environ

#store anthropic api in 'client' after getting it from the computer operating sys
client = Anthropic(
  api_key = os.getenv("DDT_API_KEY")
)

database = sqlite3.connect("fake_news.db")#automatically create fake news database
cursor = database.cursor() #object tht carries out commands

#get cursor to tell SQLite to create table only if a current "history" table does not exist, coming in 3 columns: id, article, and AI response
cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
  id INTEGER PRIMARY KEY,
  article TEXT,
  response TEXT
)
"""
)

database.commit() #save changes permanently to sqlite

suspicious_phrases=[
  ""
]

### Main function for checking articles
def CheckFakeNews():
  print("Button working") #only in terminal (i used for debugging so its easier)

  article = news_text.get("1.0", END) #retrieve from news_text, 1st line, character 0

  prompt = f"""
You are now a fake news analyser.
Analyse the following news article (it may be provided as a link which would require you to web search or in text form).

Record:
1. A reliability score from 1-100 (state rating followed by /100)
2. If the article is Likely Real, Suspicious, or Likely Fake
3. Suspicious phrasing (only 3 phrases followed by short reason each)
4. Brief explanation (1 sentence max)

Rules:
1. Do not waste tokens
2. Do not use the heading "Fake News Analysis"
3. Do not repeat information

The maximum response length is {token_amount.get()} tokens.
This is the article you will be analysing:
{article}
"""
#""" quotation for large text, f string to include {article} ad {token_amount} without being printed as a string, prompt is set as the text so the AI gets 'prompt' before the user inputs their article


  message = client.messages.create(
  model = "claude-sonnet-5", #claude sonnet model, avoiding fable because of obscurity
  max_tokens = token_amount.get(), #tokens the AI uses to respond, lesser tokens = reduce need to purchase restore tokens (newly added slider)
  messages = [
    {
      "role": "user", #AI knows prompt is from user
      "content": prompt #AI reads this as initial content
    }
  ]
)

  response = "No response received" #returns this as default if claude does not return any text
  for block in message.content: #set up loop
    if hasattr(block, "text"): #does current text block have "text" attribute? yes = true, no = false
      response = block.text #store text from claude as "response"
      break #response found = stop loop

  
  response_text.configure(state="normal") #set to normal before AI responds or it can't edit the textbox
  response_text.delete("1.0", END) #delete from line 1 - character 0, stop deleting at END of textbox
  response_text.insert(END, response) #insert response into response textbox

  #tell cursor to put AI response along with article in sqlite
  cursor.execute(
    "INSERT INTO history (article, response) VALUES (?,?)",
    (article, response)
  )

  database.commit() #save changes permanently

  response_text.configure(state="disabled") #lock accessability once AI outputs response

###Two functions to increase or decrease tokens in slider by 1
def IncreaseToken():
  if token_amount.get() < 500: #prevent going over the maximum
    token_amount.set(token_amount.get()+10) #increments of 10

def DecreaseToken():
  if token_amount.get() >100: #prevent it going under 100 tokens
    token_amount.set(token_amount.get()-10) #only works once verified current token amount >50

root = Tk() #create main tkinter window
root.configure(bg="#D2B48C")
root.attributes("-fullscreen", True)
root.title("Fake News Analyser with AI")
main_title = ctk.CTkLabel(root, text = "AI Fake News Analyser", font = ("Arial", 40, "bold" ), fg_color="#D2B48C", text_color = "#7b5740")
main_title.pack(pady=20)

token_amount = IntVar() #synergise python with tkinter widget
token_amount.set(300) #default value

subheading1 = ctk.CTkLabel(root, text = "Article:", font = ("Arial", 20, "bold"), fg_color= "#D2B48C", text_color = "#7b5740")
subheading1.pack()
news_text = ctk.CTkTextbox(root, height=200, width=600, corner_radius = 20, border_color = "#5C4033", border_width=3, fg_color= "#D2B48C") #input dimensions
news_text.pack(pady=10) #display input box


subheading2 = ctk.CTkLabel(root, text = "AI Response:", font = ("Arial", 20, "bold"), fg_color= "#D2B48C", text_color = "#7b5740") #Subheading for AI response
subheading2.pack()
response_text = ctk.CTkTextbox(root, height=250, width = 1000, corner_radius = 20, border_color = "#5C4033", border_width=3, fg_color= "#D2B48C") #AI output dimensions
response_text.pack(pady=10) #display output box

response_text.configure(state="disabled") #set so it is unable to be modified or edited

token_slider = Scale(root, from_=100, to=500, orient = HORIZONTAL, variable=token_amount, length = 300, label = "Response Length", resolution = 10) #orientation to horizontal, default is set to display down, display settings

token_slider.pack(pady = 10) #display slider

up_but = ctk.CTkButton(root, text = "➕10", command = IncreaseToken, hover_color = "#144870", width = 30) #display settings, and link with function
up_but.pack(pady = 10) #display up button

down_but = ctk.CTkButton(root, text="➖10", command = DecreaseToken, hover_color = "#144870", width = 30) #display settings, and link with function
down_but.pack(pady = 10) #display down button

ctk.CTkButton(root, text="Analyse article 🔍", command=CheckFakeNews, hover_color = "#144870").pack(pady = 10) #text, link with CheckFakeNews function

root.mainloop() #starts event loop