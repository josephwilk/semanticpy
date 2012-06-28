from unittest import TestCase
from semanticpy.vector_space import VectorSpace
from pprint import pprint
from nose.tools import *

class TestVectorSpace(TestCase):

    documents = ["The cat in the hat disabled", "A cat is a fine pet ponies.", "Dogs and cats make good pets.","I haven't got a hat."]

    def it_should_search_test(self):
        vector_space = VectorSpace(self.documents)

        pprint(vector_space.search(["cat"]))

    def it_should_find_related(self):
        vector_space = VectorSpace(self.documents)

        pprint(vector_space.related(0))