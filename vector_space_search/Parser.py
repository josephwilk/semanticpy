from porter_stemmer import PorterStemmer

class Parser:
    STOP_WORDS_FILE = 'data/english.stop'

	#A processor for removing the commoner morphological and inflexional endings from words in English
    stemmer = None
    stopwords = []

    def __init__(self,):
    	self.stemmer = PorterStemmer()
    	self.stopwords = open(Parser.STOP_WORDS_FILE, 'r').read().split()

    def tokenise_and_remove_stop_words(self, document_list):
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
