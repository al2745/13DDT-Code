from tkinter import *
from anthropic import Anthropic
import time
import requests
import os

client = Anthropic(
  api_key = ""
)

def CheckFakeNews():

  print("Test: Button is working.")

  article = news_text.get("1.0", END)

  prompt = f"""
You are now a fake news analyser.
Analyse the following news article (it may be provided as a link or in text form).

Record:
1. A reliability score from 1-100
2. If the article is Likely Real, Suspicious, or Likely Fake
3. Suspicious phrasing
4. Brief explanation

This is the article you will be analysing:
{article}
"""

  message = client.messages.create(
  model = "claude-sonnet-4-5",
  max_tokens = 300,
  messages = [
    {
      "role": "user",
      "content": prompt
    }
  ]
)

  print(message.content[0].text)

root = Tk()
news_text = Text(root, height=10, width=50) 
news_text.pack()

Button(
  root, text="Check Fake News", command=CheckFakeNews 
).pack()

root.mainloop()

