import addsubtotest #filename to test
import pytest

def test_add():
    # assert looks for boolean response
    # comparison, in, not in, is also used
    assert addsubtotest.addition(4,5) == 9

def test_sub():
    assert addsubtotest.substraction(4,5) == -1

# run in terminal:
# python -m pytest test.py
def test_word_count():
    assert addsubtotest.word_count('some text') < 10

def test_char_count():
    assert addsubtotest.char_count('input_value lorepm ipsuminput_value lorepm ipsuminput_value lorepm ipsuminput_value lorepm ipsuminput_value lorepm ipsuminput_value lorepm ipsum') < 50