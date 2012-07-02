from semanticpy.transform.transform import Transform
from vendor.onlineldavb.onlineldavb import OnlineLDA

class LDA(Transform):
    NUMBER_OF_TOPICS = 100

    def __init__(self, matrix):
        Transform.__init__(self, matrix)
        self.document_total = len(self.matrix)

    def transform(self):
        lda = OnlineLDA(vocab, NUMBER_OF_TOPICS, self.document_total, 1./NUMBER_OF_TOPICS, 1./NUMBER_OF_TOPICS, 1024., 0.7)

