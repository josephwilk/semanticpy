from unittest import TestCase
from semanticpy.transform.lsa import LSA
from nose.tools import *
import numpy

class LSATest(TestCase):
   """ """
   EPSILON = 4.90815310617e-09

   @classmethod
   def same(self, matrix1, matrix2):
    difference = matrix1 - matrix2
    max = numpy.max(difference)
    return (max <= LSATest.EPSILON)

   def it_should_do_lsa_test(self):
     matrix = [[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
               [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
               [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
               [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

     expected = [[ 0.02284739,  0.06123732,  1.20175485,  0.02284739,  0.02284739, 0.88232986,  0.03838993,  0.03838993,  0.82109254],
                 [-0.00490259,  0.98685971, -0.04329252, -0.00490259, -0.00490259, 1.02524964,  0.99176229,  0.99176229,  0.03838993],
                 [ 0.99708227,  0.99217968, -0.02576511,  0.99708227,  0.99708227, 1.01502707, -0.00490259, -0.00490259,  0.02284739],
                 [-0.0486125 , -0.13029496,  0.57072519, -0.0486125 , -0.0486125 , 0.25036735, -0.08168246, -0.08168246,  0.3806623 ]]

     expected = numpy.array(expected)
     lsa = LSA(matrix)
     new_matrix = lsa.transform()

     eq_(LSATest.same(new_matrix, expected), True)