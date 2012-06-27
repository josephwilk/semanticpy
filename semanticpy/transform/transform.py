from semanticpy.matrix_formatter import MatrixFormatter
from scipy import array

class Transform:
    def __init__(self, matrix):
        self.matrix = array(matrix, dtype=float)

    def __repr__(self):
        MatrixFormatter(self.matrix).pretty_print
