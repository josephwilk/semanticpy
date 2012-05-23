from vector_space_search.parser import Parser

class TestParser:
  """"""
  def it_should_remove_the_stop_words_test(self):
    parser = Parser()
    parser.tokenise_and_remove_stop_words(["words"])
  