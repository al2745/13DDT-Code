import requests
from bs4 import BeautifulSoup

def url_mode(url):
  webpage = requests.get(url) #ask webpage for html
  bs = BeautifulSoup(webpage.text, "html.parser") #converts into a format python can read
  paragraphs = bs.find_all("p") #filtering through paragraphs, makes claudes job easier
  full_article = "" #compile everything as one string

  for paragraph in paragraphs: #loops through every paragraph on the page
    full_article += paragraph.get_text() + "\n" #continually adds paragraphs inside full_article with a line inbetween
  return full_article #returns final text, this is the one claude reads