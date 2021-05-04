from main import *

def test_ceaser_cipher_encode_normal():
    assert ceaser_cipher_encode("abc", 1) == "bcd"
    
def test_ceaser_cipher_encode_normal_overflow():
    assert ceaser_cipher_encode("xyza", 1) == "yzab"

def test_ceaser_cipher_encode_words():
    assert ceaser_cipher_encode("hello my name is mr habib", 2) == "jgnnq oa pcog ku ot jcdkd"

def test_ceaser_cipher_encode_ignore_symbols():
    assert ceaser_cipher_encode("woah! there. are. a` few ~symbols here :j", 6) == "cugn! znkxk. gxk. g` lkc ~yeshury nkxk :p"

def test_ceaser_cipher_encode_large_shift():
    assert ceaser_cipher_encode("there is a large shift in power here", 30) == "xlivi mw e pevki wlmjx mr tsaiv livi"
 
def test_ceaser_cipher_encode_empty_string():
    assert ceaser_cipher_encode("", 1) == ""
    
def test_ceaser_cipher_encode_no_shift():
    assert ceaser_cipher_encode("hello there", 0) == "hello there"
