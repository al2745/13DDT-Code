### IMPORTS



import tkinter
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image
from tkinter import *
import customtkinter as ctk
from anthropic import Anthropic
import time
import requests
import os
from dotenv import load_dotenv
import sqlite3
from bs4 import BeautifulSoup 
#importing all external modules that will be needed for the program, most are added along the way for debugging or improvement purposes



### CLAUDE API SET UP, MAIN FUNCTION, AND DATABASE



load_dotenv() #load environmental variables from os.environ, reads .env file

#store anthropic api in 'client' after getting it from the computer operating sys
client = Anthropic(
  api_key = os.getenv("DDT_API_KEY")
)

database = sqlite3.connect("fake_news.db")#automatically create fake news database
cursor = database.cursor() #object tht carries out commands
cursor
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

analysis_mode = "Content" #current analysis mode, can vary

#runs whenever user changes modes from notebook
def ModeChange(event):
  global analysis_mode
  analysis_mode = notebook.tab(notebook.select(), "text")

#downloads html content from article site and converts it into text format, allowing claude to analyse url's
def URLMode(url):
  webpage = requests.get(url) #ask webpage for html
  bs = BeautifulSoup(webpage.text, "html.parser") #converts into a format python can read
  paragraphs = bs.find_all("p") #filtering through paragraphs, makes claudes job easier
  full_article = "" #compile everything as one string

  for paragraph in paragraphs: #loops through every paragraph on the page
    full_article += paragraph.get_text() + "\n" #continually adds paragraphs inside full_article with a line inbetween
  return full_article #returns final text, this is the one claude reads


### Main function for checking articles
def CheckFakeNews():
  print("Button working") #only in terminal (i used for debugging so its easier)

  if analysis_mode == "URL":
    url = news_text.get("1.0", END).strip() #retrieve from news_text, 1st line, character 0
    article = URLMode(url)
  else:
    article = news_text.get("1.0", END)

  prompt = f"""
You are now a fake news analyser.
Analyse the following news article (it may be provided as a link which would require you to web search or in text form).

Your analysis mode:
{analysis_mode}

If mode is:
> Content: Analyse the content only.
> URL: Enter the webpage, read the article, and analyse.
> Title: Analyse the title only.
> All: Detect what the user has inputted and analyse from that judgement.

Record:
1. A reliability score from 1-100 (state rating followed by /100)
2. If the article is Likely Real, Suspicious, or Likely Fake
3. Suspicious phrasing (only 3 phrases followed by short reason each)
4. Brief explanation (1 sentence max)

Rules:
1. Do not waste tokens
2. Do not use the heading "Fake News Analysis"
3. Do not repeat information
4. Do not refer to the analysis mode

The maximum response length is {token_amount.get()} tokens.
This is the article you will be analysing:
{article}
"""
#""" quotation for large text, f string to include {article} ad {token_amount} without being printed as a string, prompt is set as the text so the AI gets 'prompt' before the user inputs their article


  message = client.messages.create(
  model = "claude-haiku-4-5-20251001", #claude sonnet model, avoiding fable because of obscurity
  max_tokens = token_amount.get(), #tokens the AI uses to respond, lesser tokens = reduce need to purchase restore tokens (newly added slider)
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

  database.commit() #save changes permanently, TO-DO: one database commit for every cursor command?

  response_text.configure(state="disabled") #lock accessability once AI outputs response

###Two functions to increase or decrease tokens in slider by 1
def IncreaseToken():
  current_token = token_amount.get()
  if current_token < 500:
    addten_token = current_token + 10
    token_amount.set(addten_token)

    AmountUpdated(addten_token)

def DecreaseToken():
  current_token = token_amount.get() 
  if current_token >100: #prevent it going under 100 tokens
    addten_token = current_token - 10
    token_amount.set(addten_token) #only works once verified current token amount >50

    AmountUpdated(addten_token)

#updating text depending on current token amount
def AmountUpdated(value):
  tokens = token_amount.get()

  if tokens <= 230:
    ulabel.configure(text = "SHORT RESPONSE", font = ("Arial", 15, "bold"))

  elif tokens <= 370:
    ulabel.configure(text = "MEDIUM RESPONSE", font = ("Arial", 15, "bold"))

  else:
    ulabel.configure(text = "LARGE RESPONSE", font = ("Arial", 15, "bold"))


### TKINTER AND DISPLAY SETTINGS ###



root = Tk() #create main tkinter window
root.configure(bg="#D2B48C") #program background colour, went for newspaper looking biege
root.attributes("-fullscreen", True) #auto fullscreen instead of a default tiny window
root.title("Fake News Analyser with AI") #window title, NOT main title
main_title = ctk.CTkLabel(root, text = "AI Fake News Analyser", font = ("Arial", 40, "bold" ), fg_color="#D2B48C", text_color = "#7b5740") #displays on the actual gui
main_title.pack(pady=20)

notebook = ttk.Notebook(root)

content = Frame(notebook)
url = Frame(notebook)
title = Frame(notebook)
all = Frame(notebook)

# notebooks / to-do: what other options, notebook currently takes up larger visual space
notebook.add(content, text = "Content")
notebook.add(url, text = "URL")
notebook.add(title, text = "Title")
notebook.add(all, text = "All")
notebook.pack()

notebook.bind("<<NotebookTabChanged>>", ModeChange)

#labels
Label(content, width = 2, height = 1).pack()
Label(url, width = 2, height = 1).pack()
Label(title, width = 2, height = 1).pack()
Label(all, width = 2, height = 1).pack()

token_amount = IntVar() #synergise python with tkinter widget
token_amount.set(300) #default value

subheading1 = ctk.CTkLabel(root, text = "Article:", font = ("Arial", 20, "bold"), fg_color= "#D2B48C", text_color = "#7b5740")
subheading1.pack()
news_text = ctk.CTkTextbox(root, height=200, width=600, corner_radius = 25, border_color = "#5C4033", border_width=3, fg_color= "#D2B48C") #input dimensions
news_text.pack(pady=5) #display input box


subheading2 = ctk.CTkLabel(root, text = "AI Response:", font = ("Arial", 20, "bold"), fg_color= "#D2B48C", text_color = "#7b5740") #Subheading for AI response
subheading2.pack()
response_text = ctk.CTkTextbox(root, height=250, width = 1000, corner_radius = 25, border_color = "#5C4033", border_width=3, fg_color= "#D2B48C") #AI output dimensions
response_text.pack(pady=5) #display output box

response_text.configure(state="disabled") #set so it is unable to be modified or edited

slider_label = ctk.CTkLabel(root, text="Token Amount / AI Response Length", font = ("Arial", 20, "bold"), justify = CENTER) #seperate label for token slider because label cannot have centre properties when inside tslider attributes
slider_label.pack() #show label

ulabel = ctk.CTkLabel(root, text = "MEDIUM RESPONSE", font = ("Arial", 15, "bold")) #default text for updater label
ulabel.pack()

tslider = ctk.CTkSlider(root, from_=100, to=500, variable=token_amount, orientation = "horizontal", width = 300, number_of_steps= 40, command = AmountUpdated) #orientation to horizontal, default is set to display down, display settings
tslider.pack(pady = 5) #display slider

up_but = ctk.CTkButton(root, text = "+10", fg_color = "#144870", corner_radius = 25, command = IncreaseToken, hover_color = "#0C395B", width = 20) #display settings, and link with function
up_but.pack(pady = 5) #display up button

down_but = ctk.CTkButton(root, text="-10", fg_color = "#144870", corner_radius = 25, command = DecreaseToken, hover_color = "#0C395B", width = 20) #display settings, and link with function
down_but.pack(pady = 5) #display down button

ctk.CTkButton(root, text="ANALYSE ARTICLE 🔍", font = ("Arial", 20, "bold"), fg_color = "#144870", corner_radius = 25, height = 50, command=CheckFakeNews, hover_color = "#0C395B").pack(pady = 10) #text, link with CheckFakeNews function

root.mainloop() #starts event loop


### TO-DO LIST
# - Navigation menu : analyse by content, url, title, all