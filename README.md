# Astana IT University: Blockchain Hack 2023 

## Project name

DaVinci Analysis

## Selected problem

Crypto market news impact analyzer: Correlation of news sentiment with token price movements

## Team name

DaVinci

## Participants

* Full name: Zeylan Emir. Email: emir.zeilan@gmail.com


## Abstract

DaVinci Analysis — your innovative cryptotool
## Demo video

https://youtu.be/mpPje7OKYEM

## How to run

Clone the entire repository from github

Then open the VSCode

Log in to index.html and run the Live Server extension (if any)


To launch the chatbot from the Langchain file, log into the terminal in VS Code, then enter the streamlit run Langchain.py

To work with a chatbot bitcoin_bot.py it is necessary to enter your own question in the "answer" field in the code, and then run the code through the terminal by entering the python command bitcoin_bot.py



### Prerequisites:

To launch the project, please install the following extensions:

pip install longchain

pip install numpy

pip install embedding chain

### Running

Clone the entire repository from github

Then open the VSCode

Log in to index.html and run the Live Server extension (if any)


To launch the chatbot from the Langchain file, log into the terminal in VS Code, then enter the streamlit run Langchain.py

To work with a chatbot bitcoin_bot.py it is necessary to enter your own question in the "answer" field in the code, and then run the code through the terminal by entering the python command bitcoin_bot.py
## Inspirations

The main inspiration for this idea was the Sentiment resource, or rather its extreme circumcision due to the fact that the "communication with price charts" function does not work on the site, as well as extremely dubious AI answers on the market, extreme confusion and lack of complete analytics coupled with a "manual" search from other users prompted to correct this situation. The main essence of DaVinci Analysis is the integration of ChatGPT itself into the API, i.e. not just connection, but semantic integration for a clearer understanding and tracking, as well as analysis of news and the state of the cryptocurrency market.

## Technology stack and organization

Langchain, Python, Embedchain, HTML&CSS&JS

## Solutions and features implemented

1. Displaying the news listing on the main page
2. A more correct display of the token price in both graphical and metallic form
3. Chatbot with semantics and context of API and various news (intentionally limited for stress test but running on GPT-4 version)
4. Chatbot on Langchain with DuckAndGo connected

## Challenges faced
What has not been implemented:

AI Forum — A function that allowed both professional analysts and beginners to discuss, GPT-4 was supposed to "read" every discussion from the forum and, in the form of summarize, issue its verdict on the announced arguments and identify misinformation (by parsing information through the serp api)

Newbie is a page for beginners where AI based on articles for beginners would advise investing in certain tokens or displays more "Easy" statistics with an explanation of all terms


Oraculus Api:

1) Due to the lack of documentation in the form of yaml, I had to "tinker" a little and try to find the most convenient solution for integrating the Oraculus Api into GPT-4

2) Insufficient context in the information provided by the JSON Api, for example, the same Bitcoin price gives only the time and amount of bitcoin in USD, while GPT-4 does not always have the right context and trying to answer the question "The cost of Bitcoin now?" he can't catch the context in the API

((I'm coming from personal experience, perhaps due to lack of experience with large memory dumps, I may be wrong!!!)
3) The CSV dump is too large, personally it was difficult for me to process it or translate it into JSON, it would be better if the API initially included the history of the last 100 transactions and not just 1 during a particular day

## Lessons learned

Skills have been mastered:

Python, Langchain, Embedchain, Javascript and handling large dumps

## Future work

It is necessary to finish AIForum and Newbie analytics and also supplement Pro Analytics AI with Graphs with analysis in the form of summarize
#   D a V i n c i - A n a l y s i s - A s t a n a - I T - U n i v e r s i t y - B l o c k c h a i n - H a c k - 2 0 2 3 
 
 #   D a V i n c i - A n a l y s i s - A s t a n a - I T - U n i v e r s i t y - B l o c k c h a i n - H a c k - 2 0 2 3 
 
 
