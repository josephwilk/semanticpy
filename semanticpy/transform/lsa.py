from scipy import linalg,dot

from transform import Transform

class LSA(Transform):
    """ Latent Semantic Analysis(LSA).
	    Apply transform to a document-term matrix to bring out latent relationships.
	    These are found by analysing relationships between the documents and the terms they 
	    contain.
    """

    def transform(self, dimensions=1):
		""" Calculate SVD of objects matrix: U . SIGMA . VT = MATRIX 
		    Reduce the dimension of sigma by specified factor producing sigma'. 
		    Then dot product the matrices:  U . SIGMA' . VT = MATRIX'
		"""
		rows,cols = self.matrix.shape

		if dimensions <= rows: #Its a valid reduction

			#Sigma comes out as a list rather than a matrix
			u,sigma,vt = linalg.svd(self.matrix)

			#Dimension reduction, build SIGMA'
			for index in xrange(rows - dimensions, rows):
				sigma[index] = 0

			#Reconstruct MATRIX'
			transformed_matrix = dot(dot(u, linalg.diagsvd(sigma, len(self.matrix), len(vt))) ,vt)

			return transformed_matrix

		else:
			print "dimension reduction cannot be greater than %s" % rows