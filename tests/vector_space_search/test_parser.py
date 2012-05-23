import unittest
from vector_space_search.parser import Parser
from nose.tools import *

class TestParser(unittest.TestCase):
  def setUp(self):
    self.parser = Parser()
    
  def it_should_remove_the_stop_words_test(self):
    parsed_words = self.parser.tokenise_and_remove_stop_words(["a", "sheep"])
    eq_(parsed_words,["sheep"])
  
  def it_should_stem_words_test(self):
    parsed_words = self.parser.tokenise_and_remove_stop_words(["monkey"])
    eq_(parsed_words,["monkei"])

  def it_should_remove_grammar_test(self):
    parsed_words = self.parser.tokenise_and_remove_stop_words(["sheep..."])
    eq_(parsed_words, ["sheep"])