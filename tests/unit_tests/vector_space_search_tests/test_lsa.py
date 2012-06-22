from unittest import TestCase
from semanticpy.vector_space_search.lsa import LSA
from nose.tools import *

class TestLSA(TestCase):
   """ """
   def it_should_do_something_test(self):
     matrix = [[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
               [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
               [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

     lsa = LSA(matrix)
     pass