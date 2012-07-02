from math import *
from transform import Transform

class TFIDF(Transform):

    def __init__(self, matrix):
        Transform.__init__(self, matrix)
        self.document_total = len(self.matrix)


    def transform(self):
        """ Apply TermFrequency(tf)*inverseDocumentFrequency(idf) for each matrix element.
        This evaluates how important a word is to a document in a corpus

        With a document-term matrix: matrix[x][y]
        tf[x][y] = frequency of term y in document x / frequency of all terms in document x
        idf[x][y] = log( abs(total number of documents in corpus) / abs(number of documents with term y)  )
        Note: This is not the only way to calculate tf*idf
        """

        rows,cols = self.matrix.shape
        transformed_matrix = self.matrix.copy()

        for row in xrange(0, rows): #For each document

            word_total = reduce(lambda x, y: x+y, self.matrix[row] )
            word_total = float(word_total)

            for col in xrange(0, cols): #For each term
                transformed_matrix[row,col] = float(transformed_matrix[row,col])

                if transformed_matrix[row][col] != 0:
                    transformed_matrix[row,col] = self._tf_idf(row, col, word_total)

        return transformed_matrix


    def _tf_idf(self, row, col, word_total):
        term_frequency = self.matrix[row][col] / float(word_total)
        inverse_document_frequency = log(abs(self.document_total / float(self._get_term_document_occurences(col))))
        return term_frequency * inverse_document_frequency


    def _get_term_document_occurences(self, col):
        """ Find how many documents a term occurs in"""

        term_document_occurrences = 0

        rows, cols = self.matrix.shape

        for n in xrange(0,rows):
            if self.matrix[n][col] > 0: #Term appears in document
                term_document_occurrences +=1
        return term_document_occurrences
