from unittest import TestCase
from semanticpy.vector_space import VectorSpace
from pprint import pprint
from nose.tools import *

class TestVectorSpace(TestCase):

    documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]

    def it_should_search_test(self):
        vector_space = VectorSpace(self.documents, transforms = [])

        eq_(vector_space.search(["cat"]), [0.5773502691896258, 0.5, 0.4472135954999579, 0.0])

    def it_should_find_related(self):
        vector_space = VectorSpace(self.documents)

        eq_(vector_space.related(0), [])