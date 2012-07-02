from unittest import TestCase
from semanticpy.vector_space import VectorSpace
from pprint import pprint
from nose.tools import *

class VectorSpaceTest(TestCase):

    documents = ["cat", "cat dog","hat"]

    def it_should_search_test(self):
        vector_space = VectorSpace(self.documents, transforms = [])

        eq_(vector_space.search(["cat"]), [1.0, 0.7071067811865475, 0.0])

    def it_should_find_related_test(self):
        vector_space = VectorSpace(self.documents)

        eq_(vector_space.related(0), [1.0000000000000002, 0.9999999999999998, 0.0])