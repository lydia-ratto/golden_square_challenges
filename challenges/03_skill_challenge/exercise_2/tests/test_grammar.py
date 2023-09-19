import pytest
from lib.grammar import *

def test_capitalised_first_word_full_stop_end():
    assert verify_text_grammar('Hello and welcome to Makers.') == True

def test_capitalised_first_word_no_full_stop_end():
    assert verify_text_grammar('Hello and welcome to Makers') == False

def test_lowercase_first_word_full_stop_end():
    assert verify_text_grammar('hello and welcome to Makers.') == False

def test_lowercase_first_word_no_full_stop_end():
    assert verify_text_grammar('hello and welcome to Makers') == False