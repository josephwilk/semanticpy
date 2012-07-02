from unittest import TestCase
from semanticpy.vector_space import VectorSpace
from nose.tools import *


class TestSemanticPy(TestCase):
    def setUp(self):
        self.documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]
    
    def it_should_search_test(self):
        vectorSpace = VectorSpace(self.documents)
  	
        eq_(vectorSpace.search(["cat"]), [0.14487566959813258, 0.1223402602604157, 0.07795622058966725, 0.05586504042763477])

    def it_should_find_return_similarity_rating_test(self):
        vectorSpace = VectorSpace(self.documents)

        eq_(vectorSpace.related(0), [1.0, 0.9922455760198575, 0.08122814162371816, 0.0762173599906487])