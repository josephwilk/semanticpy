import os
from porter_stemmer import PorterStemmer
import os

class Parser:
    STOP_WORDS_FILE = '%s/../data/english.stop' %  os.path.dirname(os.path.realpath(__file__))

    stemmer = None
    stopwords = []

    def __init__(self, stopwords_io_stream = None):
    	self.stemmer = PorterStemmer()
        
        if(not stopwords_io_stream):
    	  stopwords_io_stream = open(Parser.STOP_WORDS_FILE, 'r')

        self.stopwords = stopwords_io_stream.read().split()

    def tokenise_and_remove_stop_words(self, document_list):
        if not document_list:
          return []
          
    	vocabulary_string = " ".join(document_list)
                
    	tokenised_vocabulary_list = self._tokenise(vocabulary_string)
    	clean_word_list = self._remove_stop_words(tokenised_vocabulary_list)
        return clean_word_list

    def _remove_stop_words(self, list):
    	""" Remove common words which have no search value """
    	return [word for word in list if word not in self.stopwords ]


    def _tokenise(self, string):
    	""" break string up into tokens and stem words """
    	string = self._clean(string)
    	words = string.split(" ")
		
    	return [self.stemmer.stem(word, 0, len(word)-1) for word in words]

    def _clean(self, string):
    	""" remove any nasty grammar tokens from string """
    	string = string.replace(".","")
    	string = string.replace("\s+"," ")
    	string = string.lower()
    	return string
