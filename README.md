***AI Fake News Analyser***

**Purpose of Program:**
AI powered tool to analyse any given article, judging it based on its validity, phrasing, and reliability. 
The program provides 4 different analysis modes:
- Content
- URL
- Title
- All

Anthropic API is used to generate the analysis and is stored in the SQLite database.

**Requirements to Run:**
- Python version 3
- Internet connection
- Anthropic API Key
- Libraries found below

**Library Installations:**
In terminal/command prompt, enter the folder with app.py, then:
- Mac: pip3 install anthropic python-dotenv requests beautifulsoup4 customtkinter pillow
- Windows: py -m pip install anthropic python-dotenv requests beautifulsoup4 customtkinter pillow
- Windows 2nd Option: python -m pip install anthropic python-dotenv requests beautifulsoup4 customtkinter pillow

**API Key Setup:**
For security precautions, the personal API key I have used in the development process will not be provided. However, a separate moderation key will be given.
Once the project has been opened, create a file named .env in the same folder as app.py. Then inside the .env file, enter this, along with the given API key:
DDT_API_KEY=the_given_api_key_here

**Running the Program:**
Click run, choose the analysis mode at the top, paste an article you want to test into the input box, modify the token spending/amount to your liking, then press "Analyse Article". You should receive a response based on the claude AI.

**Tokens Usage:**
For measurement purposes, the token range is only between 100 - 500. There is currently only $4.87 worth of credits left in the anthropic account as of Monday 24th August, with a running rate of $1 / MTok for input, and $5 / MTok for output. While the chance is low, avoid overspending tokens often (unnecessarily long articles) so that there is no risk of the account going running out of credits for future moderation. Roughly 400 input tokens and 300 output tokens will do just fine and can be considered a normal standard. For an average spending of 500 input tokens and 300 output tokens, it would last around 2435 analyses. The aim is to preserve a generous amount of usages until the end of January 2026.

**Database:**
After running, a database will be created in your folder where you will be able to view previously analysed articles.
