from pprint import pprint
from Parser import Parser
from sets import Set
import sys

try:
	from numpy import dot
	from numpy.linalg import norm
except:
	print "Error: Requires numpy from http://www.scipy.org/. Have you installed scipy?"
	sys.exit() 

class VectorSpace:
	""" A algebraic model for representing text documents as vectors of identifiers. 
	A document is represented as a vector. Each dimension of the vector corresponds to a 
	separate term. If a term occurs in the document, then the value in the vector is non-zero.
	"""

	#Collection of document term vectors
	document_vectors = []

	#Mapping of vector index to keyword
	vector_keyword_index=[]

	#Tidies terms
	parser=None


	def __init__(self, documents=[]):
		self.document_vectors=[]
		self.parser = Parser()
		if(len(documents)>0):
			self.build(documents)


	def build(self,documents):
		""" Create the vector space for the passed document strings """
		self.vector_keyword_index = self.get_vector_keyword_index(documents)

		self.document_vectors = [self.make_vector(document) for document in documents]


	def get_vector_keyword_index(self, documentList):
		""" create the keyword associated to the position of the elements within the document vectors """
		vocabulary_list = self.parser.tokenise_and_remove_stop_words(documentList)
        unique_vocabulary_list = self._remove_duplicates(vocabulary_list)
		
		vectorIndex={}
		offset=0
		#Associate a position with the keywords which maps to the dimension on the vector used to represent this word
		for word in uniqueVocabularyList:
			vectorIndex[word]=offset
			offset+=1
		return vectorIndex  #(keyword:position)


	def make_vector(self, wordString):
		""" @pre: unique(vectorIndex) """

		#Initialise vector with 0's
		vector = [0] * len(self.vector_keyword_index)

		word_list = self.parser.tokenise_and_remove_stop_words(documentList)

		for word in wordList:
			vector[self.vector_keyword_index[word]] += 1; #Use simple Term Count Model
		return vector


	def build_query_vector(self, termList):
		""" convert query string into a term vector """
		query = self.make_vector(" ".join(termList))
		return query


	def related(self,documentId):
		""" find documents that are related to the document indexed by passed Id within the document Vectors"""
		ratings = [util.cosine(self.document_vectors[documentId], documentVector) for documentVector in self.document_vectors]
		ratings.sort(reverse=True)
		return ratings


	def search(self,searchList):
		""" search for documents that match based on a list of terms """
		queryVector = self.build_query_vector(searchList)

		ratings = [util.cosine(queryVector, documentVector) for documentVector in self.document_vectors]
		ratings.sort(reverse=True)
		return ratings
        
    

    def _remove_duplicates(list):
        """ remove duplicates from a list """
        return Set((item for item in list))
    
        
    def _cosine(vector1, vector2):
    	""" related documents j and q are in the concept space by comparing the vectors :
    		cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
    	return float(dot(vector1,vector2) / (norm(vector1) * norm(vector2)))

if __name__ == '__main__':
	#test data
	documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]

	vectorSpace= VectorSpace(documents)
	pprint(vectorSpace.related(0))
	pprint(vectorSpace.search(["cat"]))

