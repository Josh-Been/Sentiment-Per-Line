# Sentiment-Per-Line
Sentiment values per line in text file. Results downloaded to structured csv table.
Baylor University Libraries: Implementation of VaderSentiment

This Python application was created by the Baylor University Libraries to assist researchers to apply sentiment to text files using the VaderSentiment library. Baylor University has no connection with the creator of the VaderSentiment library. This is merely a browsable form to access the library. For documentation of the VaderSentiment library, navigate to https://github.com/cjhutto/vaderSentiment.

VADER (Valence Aware Dictionary and sEntiment Reasoner)

This application will create a comma delimited spreadsheet in the same directory as the selected settings file. The spreadsheet will repeat each line in the first column and write the assigned composite sentiment in the second column.

__Steps__

(1) Ensure Python 2.7 is installed on your computer. The advised package is Anaconda Python, available here https://www.anaconda.com/download

(2) Ensure that you have the proper Python libraries to run the application. This requires the standard Python libraries provided by the Anaconda2 distribution, as well as the PIL (https://anaconda.org/anaconda/pil) and VaderSentiment libraries (pip install vaderSentiment).\n')

(3) Click the Browse for Text File to Run Vader Sentiment button.

(4) This will create a comma delimited spreadsheet in the same directory as the selected settings file.
 
 Licensed under the MIT License
 Under production
 
 Developed using Python Anaconda2, 64 bit
 Dependencies not included in Anaconda2: VaderSentiment, PIL
 Additional dependencies: Tkinter, operator, string, webbrowser, os, subprocess

__Setup Instructions for Those New to Python__

(1) First, download the script repository. Click the green 'Clone or Download' button and select 'Download Zip.' Extract the .zip contents.

(1) Second is to install Python. Install Anaconda Python 2.7 from https://www.anaconda.com/download/

(2) Third is to add any additional Python libraries the script requires using the command line. On a Mac, open Terminal (CMD-Space and type terminal and enter). On a PC, launch 'Anaconda Prompt' from the Anaconda2 application directory. Type three words: pip install _name of library_. If Tweepy needed installation, for example, type: pip install Tweepy. Do this for each additional library required by the script. This permanently installs these libraries onto your computer, so you will not need to reinstall these libraries a second time.

(3) Fourth and finally is to run the script using Anaconda Spyder. Launch the Anaconda Navigator application, which is a menu of applications included within Anaconda, and then launch Spyder. File/Open and browse to the .py Python script downloaded in step 1. Press the green 'Run File' button (or click F5). If you do not see anything happening, check the monimized windows for the application.
