from tkinter import *
import openai
print(openai.__version__)
from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);

def CheckNews():
    fake_words = [
    "alien",
    "ufo",
    "conspiracy",
    "hoax",
    "miracle",
    "secret",
    "shocking",
    "unbelievable",
    "exposed",
    "clickbait",
    "scandal",
    "coverup",
    "mind-control",
    "government lies",
    "cure-all",
    "100% proof",
    "guaranteed",
    "breaking",
    "sensational",
    "outrageous"
]