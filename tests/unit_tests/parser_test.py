from unittest import TestCase
from semanticpy.parser import Parser
from nose.tools import *

class ParserTest(TestCase):
  class FakeStopWords:
    def __init__(self, stop_words=''):
      self.stop_words = stop_words

    def read(self):
      return self.stop_words

  def create_parser_with_stopwords(self, words_string):
    return Parser(ParserTest.FakeStopWords(words_string))
  
  def create_parser(self):
    return Parser(ParserTest.FakeStopWords())
    
  def it_should_remove_the_stopwords_test(self):
    parser = self.create_parser_with_stopwords('a')
    
    parsed_words = parser.tokenise_and_remove_stop_words(["a", "sheep"])
    
    eq_(parsed_words, ["sheep"])
  
  def it_should_stem_words_test(self):
    parser = self.create_parser()
    
    parsed_words = parser.tokenise_and_remove_stop_words(["monkey"])
    
    eq_(parsed_words, ["monkei"])

  def it_should_remove_grammar_test(self):
    parser = self.create_parser()
    
    parsed_words = parser.tokenise_and_remove_stop_words(["sheep..."])
    
    eq_(parsed_words, ["sheep"])
    
  def it_should_return_an_empty_list__when_words_string_is_empty_test(self):
    parser = self.create_parser()
    
    parsed_words = parser.tokenise_and_remove_stop_words([])
    
    eq_(parsed_words, [])