from unittest import TestCase
from vector_space_search.vector_space import VectorSpace
from nose.tools import *
from pprint import pprint

class TestVectorSpace(TestCase):
    def setUp(self):
        self.documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
    
    def it_should_search_test(self):
        vectorSpace = VectorSpace(self.documents)
  	
        eq_(vectorSpace.search(["cat"]), [0.5773502691896258, 0.5, 0.4472135954999579, 0.0])

    def it_should_find_return_similarity_rating_test(self):
        vectorSpace = VectorSpace(self.documents)

        eq_(vectorSpace.related(0), [1.0000000000000002, 0.5773502691896258, 0.2886751345948129, 0.2581988897471611])