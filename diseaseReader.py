from nltk.corpus.reader import WordListCorpusReader
#This code is supposed to actually read the word list of diseases
#and show the words correctly in the console. 
#This line uses WordListCorpusReader and sets equal to our wordlist
reader = WordListCorpusReader('.', ['wordlist'])
#Function grabs the disease words
#The code works with no errors however, the words aren't being printed. 
#I'm not sure why since my wordlist is a text file.
reader.words()
reader.fileids()

