import unittest
from vector_space_search.parser import Parser

class TestParser(unittest.TestCase):

  def setUp(self):
    self.parser = Parser()
    
  def it_should_remove_the_stop_words_test(self):
    parsed_words = self.parser.tokenise_and_remove_stop_words(["a", "sheep"])
    self.assertEqual(parsed_words,["sheep"])
  
  def it_should_stem_words_test(self):
    parsed_words = self.parser.tokenise_and_remove_stop_words(["monkey"])
    self.assertEqual(parsed_words,["monkei"])

  def it_should_remove_grammar_test(self):
    parsed_words = self.parser.tokenise_and_remove_stop_words(["sheep..."])
    self.assertEqual(parsed_words, ["sheep"])