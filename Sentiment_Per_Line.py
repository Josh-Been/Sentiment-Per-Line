#################
#Sentiment values per line in text file. Results downloaded to structured csv table.
#Baylor University Libraries: Implementation of VaderSentiment
#
#This Python application was created by the Baylor University Libraries to assist researchers to apply sentiment to text files using the VaderSentiment library. Baylor University has no connection with the creator of the VaderSentiment library. This is merely a browsable form to access the library. For documentation of the VaderSentiment library, navigate to https://github.com/cjhutto/vaderSentiment.
#VADER (Valence Aware Dictionary and sEntiment Reasoner)
#This application will create a comma delimited spreadsheet in the same directory as the selected settings file. The spreadsheet will repeat each line in the first column and write the assigned composite sentiment in the second column.
#
#__Steps__
#(1) Ensure Python 2.7 is installed on your computer. The advised package is Anaconda Python, available here https://www.anaconda.com/download
#(2) Ensure that you have the proper Python libraries to run the application. This requires the standard Python libraries provided by the Anaconda2 distribution, as well as the PIL (https://anaconda.org/anaconda/pil) and VaderSentiment libraries (pip install vaderSentiment).\n')
#(3) Click the Browse for Text File to Run Vader Sentiment button.
#(4) This will create a comma delimited spreadsheet in the same directory as the selected settings file.
# 
# Licensed under the MIT License
# Under production
# 
# Developed using Python Anaconda2, 64 bit
# Dependencies not included in Anaconda2: VaderSentiment, PIL
# Additional dependencies: Tkinter, operator, string, webbrowser, os, subprocess
#################

import os, operator, string, webbrowser, os, subprocess
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from Tkinter import *
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
from PIL import ImageTk, Image


def entry_form():
    root = Tk()
    root.title("Baylor University Libraries: VaderSentiment Line Analyzer")
    # root.wm_iconbitmap('ico.ico')

    try:
        img = ImageTk.PhotoImage(Image.open('capture.PNG'))
        panel = Label(root, image = img)
        panel.pack(side = "top", fill = "both", expand = "yes")
    except:
        print 'Passing on picture'

    txtHeader = Text(root, height=3, width=48)
    txtHeader.pack()
    txtHeader.insert(END, "VaderSentiment Line Analyzer\nDeveloped by Baylor University Libraries\nContact Joshua_Been@baylor.edu for assistance\n")

    separator = Frame(height=0, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)

    def help_file():
        f=open('helpfile.txt', 'w')
        f.write('Sentiment values per line in text file. Results downloaded to structured csv table.\n')
        f.write('Baylor University Libraries: Implementation of VaderSentiment\n\n')
        f.write('This Python application was created by the Baylor University Libraries to assist researchers to apply sentiment to text files using the VaderSentiment library. Baylor University has no connection with the creator of the VaderSentiment library. This is merely a browsable form to access the library. For documentation of the VaderSentiment library, navigate to https://github.com/cjhutto/vaderSentiment.\n')
        f.write('VADER (Valence Aware Dictionary and sEntiment Reasoner)\n')
        f.write('This application will create a comma delimited spreadsheet in the same directory as the selected settings file. The spreadsheet will repeat each line in the first column and write the assigned composite sentiment in the second column.\n\n')
        f.write('__Steps__\n')
        f.write('(1) Ensure Python 2.7 is installed on your computer. The advised package is Anaconda Python, available here https://www.anaconda.com/download\n')
        f.write('(2) Ensure that you have the proper Python libraries to run the application. This requires the standard Python libraries provided by the Anaconda2 distribution, as well as the PIL (https://anaconda.org/anaconda/pil) and VaderSentiment libraries (pip install vaderSentiment).')
        f.write('(3) Click the Browse for Text File to Run Vader Sentiment button.\n')
        f.write('(4) This will create a comma delimited spreadsheet in the same directory as the selected settings file.\n')
        f.close()
        launch(f.name)     

    def launch(url):
        if os.name == 'nt':
            command=webbrowser.open(url,new=2)
        elif 'http:' in url or 'https:' in url:
            command=webbrowser.get().open(url,new=2)
        else:
            subprocess.call(['open', '-a', 'TextEdit', url])

    def destroy():
        root.update()
        root.destroy()

    def strip_non_ascii(string):
        ''' Returns the string without non ASCII characters'''
        string = string.replace('\n','')
        string = string.replace(',','')
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)

    def processVader(txt_file):
        analyzer = SentimentIntensityAnalyzer()
        lines = txt_file
        i = 0
        while i >= 0:
            print i
            if not os.path.isfile(lines.replace('.csv',str(i) + 'Vader.csv')):
                out_file = lines.replace('.csv',str(i) + 'Vader.csv')
                break
            if not os.path.isfile(lines.replace('.txt',str(i) + 'Vader.csv')):
                out_file = lines.replace('.txt',str(i) + 'Vader.csv')
                break
            i+=1
        fout = open(out_file, 'w')   
        with open(lines) as f:
            for line in f:
                line = line.replace(',','')
                vs = analyzer.polarity_scores(line)
                fout.write(line.replace('\n','') + ',' + str(vs['compound']) + '\n')
        fout.close()
        
    def callback():
        txt_file = askopenfilename()
        if txt_file != '':
            try:
                txtSelected.set('Processing')
                processVader(txt_file)
                txtSelected.set('Job Successful!')
                root.update()
            except:
                txtSelected.set('! Problem Processing !')
            
    Button(root, text='Browse for Text File to Process Vader', fg='blue', command=callback).pack(fill=X)
    txtSelected = StringVar()
    Label(root, textvariable=txtSelected, fg='white', bg='black').pack()
    txtSelected.set('Idle...')

    # create a toplevel menu
    menubar = Menu(root)

    # display the menu
    root.config(menu=menubar)
    
    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Digital Scholarship @ Baylor", command=lambda : launch('http://blogs.baylor.edu/digitalscholarship/'))
    filemenu.add_command(label='Vader Sentiment', command=lambda : launch('https://github.com/cjhutto/vaderSentiment'))    
    menubar.add_cascade(label="Links", menu=filemenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Documentation", command=help_file)
    helpmenu.add_command(label="Contact Author", command=lambda : launch('http://researchguides.baylor.edu/prf.php?account_id=144176'))
    menubar.add_cascade(label="About", menu=helpmenu)

    menubar.add_command(label="Quit", command=destroy)

    # display the menu
    root.config(menu=menubar)
    
    mainloop()

def main():
    entry_form()

if __name__ == "__main__":
    main()
