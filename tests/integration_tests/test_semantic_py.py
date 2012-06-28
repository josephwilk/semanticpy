from unittest import TestCase
from semanticpy.vector_space import VectorSpace
from semanticpy.transform.lsa import LSA
from semanticpy.transform.tfidf import Tfidf
from semanticpy.matrix_formatter import MatrixFormatter
from scipy import array
from nose.tools import *


class TestSemanticPy(TestCase):
    def setUp(self):
        self.documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
    
    def it_should_search_test(self):
        vectorSpace = VectorSpace(self.documents)
  	
        eq_(vectorSpace.search(["cat"]), [0.5773502691896258, 0.5, 0.4472135954999579, 0.0])

    def it_should_find_return_similarity_rating_test(self):
        vectorSpace = VectorSpace(self.documents)

        eq_(vectorSpace.related(0), [1.0000000000000002, 0.5773502691896258, 0.2886751345948129, 0.2581988897471611])
        
    def it_should_do_lsa_magic_test(self):
    	#Example document-term matrix
    	# Vector dimensions: good, pet, hat, make, dog, cat, poni, fine, disabl
    	matrix=array([[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
    		[0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0], 
    		[1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0], 
    		[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])


        print MatrixFormatter(matrix).pretty_print()

        tdidf = Tfidf(matrix)
        matrix = tdidf.transform()

        print MatrixFormatter(matrix).pretty_print()

        lsa = LSA(matrix)
        matrix = lsa.transform()

        print MatrixFormatter(matrix).pretty_print()