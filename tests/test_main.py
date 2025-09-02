from src import main


def test_say_hello():
    assert main.say_hello() == "Hello!"
