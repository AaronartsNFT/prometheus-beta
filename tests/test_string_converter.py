import pytest
from src.string_converter import to_constant_case

def test_basic_string():
    assert to_constant_case("hello world") == "HELLO_WORLD"

def test_camel_case():
    assert to_constant_case("helloWorld") == "HELLO_WORLD"

def test_pascal_case():
    assert to_constant_case("HelloWorld") == "HELLO_WORLD"

def test_snake_case():
    assert to_constant_case("hello_world") == "HELLO_WORLD"

def test_mixed_case():
    assert to_constant_case("Hello_World") == "HELLO_WORLD"

def test_with_numbers():
    assert to_constant_case("hello2World") == "HELLO_2_WORLD"

def test_with_special_characters():
    assert to_constant_case("hello-world!test") == "HELLO_WORLD_TEST"

def test_empty_string():
    assert to_constant_case("") == ""

def test_single_word():
    assert to_constant_case("hello") == "HELLO"

def test_multiple_spaces():
    assert to_constant_case("hello   world") == "HELLO_WORLD"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        to_constant_case(123)

def test_with_multiple_uppercase():
    assert to_constant_case("HTTPRequest") == "HTTP_REQUEST"

def test_complex_mixed_case():
    assert to_constant_case("convertToConstantCase") == "CONVERT_TO_CONSTANT_CASE"