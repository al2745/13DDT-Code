**AI Fake News Analyser**

**Purpose**:
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

**Install Libraries:**
In terminal/command prompt, enter the folder with app.py, then:
- Mac: pip3 install anthropic python-dotenv requests beautifulsoup4 customtkinter pillow
- Windows: py -m pip install anthropic python-dotenv requests beautifulsoup4 customtkinter pillow
- Windows option 2: python -m pip install anthropic python-dotenv requests beautifulsoup4 customtkinter pillow

**API Key Setup:**
For security precautions, the personal API key I have used in the development process will not be provided. However, a separate key can be found below.
Once the project has been opened, create a file named .env in the same folder as app.py. Then inside the .env file, enter this, along with the given API key:
DDT_API_KEY=the_given_api_key_here

**Using the Program:**
Click run, choose the analysis mode at the top, paste an article you want to test into the input box, modify the token spending/amount to your liking, then press "Analyse Article". You should receive a response based on the claude AI.

For measures, the token range is only between 100 - 500.

After running, a database will be created in your folder, where you will be able to view previously analysed articles.
