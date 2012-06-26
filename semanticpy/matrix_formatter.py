class MatrixFormatter:

    def __init__(self, matrix):
        self.matrix = matrix

    def pretty_print(self):
        """ Make the matrix look pretty """
        out = ""

        rows,cols = self.matrix.shape

        for row in xrange(0,rows):
            out += "["

            for col in xrange(0,cols):
                out += "%+0.2f "%self.matrix[row][col]
            out += "]\n"

        return out