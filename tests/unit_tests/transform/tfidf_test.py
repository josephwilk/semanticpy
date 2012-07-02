from unittest import TestCase
from semanticpy.transform.tfidf import TFIDF
from nose.tools import *
import numpy

class TFIDFTest(TestCase):
    """ """
    EPSILON = 4.90815310617e-09


    @classmethod
    def same(self, matrix1, matrix2):
        difference = matrix1 - matrix2
        max = numpy.max(difference)
        return (max <= TFIDFTest.EPSILON)


    def it_should_do_tfidf_test(self):
        matrix = [[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
                  [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0],
                  [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

        expected = [[0.,         0.,             0.23104906, 0.,         0.,         0.09589402, 0.,         0.,         0.46209812],
                    [0.,         0.1732868,      0.,         0.,         0.,         0.07192052, 0.34657359, 0.34657359, 0.        ],
                    [0.27725887, 0.13862944,     0.,         0.27725887, 0.27725887, 0.05753641, 0.,         0.,         0.        ],
                    [0.,         0.,             0.69314718, 0.,         0.,         0.,         0.,         0.,         0.        ]]

        expected = numpy.array(expected)

        tfidf = TFIDF(matrix)
        new_matrix = tfidf.transform()

        eq_(TFIDFTest.same(new_matrix, expected), True)
