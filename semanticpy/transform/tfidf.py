from math import *
from transform import Transform

class Tfidf(Transform):

    def __get_term_document_occurences(self,col):
        """ Find how many documents a term occurs in"""

        term_document_occurences = 0

        rows,cols = self.matrix.shape

        for n in xrange(0,rows):
            if self.matrix[n][col]>0: #Term appears in document
                term_document_occurences+=1
        return term_document_occurences


    def transform(self,):
        """ Apply TermFrequency(tf)*inverseDocumentFrequency(idf) for each matrix element.
              This evaluates how important a word is to a document in a corpus

              With a document-term matrix: matrix[x][y]
              tf[x][y] = frequency of term y in document x / frequency of all terms in document x
              idf[x][y] = log( abs(total number of documents in corpus) / abs(number of documents with term y)  )
              Note: This is not the only way to calculate tf*idf
          """

        document_total = len(self.matrix)
        rows,cols = self.matrix.shape

        for row in xrange(0, rows): #For each document

            word_total= reduce(lambda x, y: x+y, self.matrix[row] )

            for col in xrange(0,cols): #For each term

                #For consistency ensure all self.matrix values are floats
                self.matrix[row][col] = float(self.matrix[row][col])

                if self.matrix[row][col]!=0:

                    term_document_occurences = self.__get_term_document_occurences(col)

                    term_frequency = self.matrix[row][col] / float(word_total)
                    inverse_document_frequency = log(abs(document_total / float(term_document_occurences)))
                    self.matrix[row][col] = term_frequency * inverse_document_frequency
