from zeither import __version__
from zeither import Either


def test_version():
    assert __version__ == "0.1.0"


def test_either_map():
    either = Either(1)
    assert either.map(lambda x: x + 1).value == 2


def test_either_map_left_side():
    either = Either(1, False)
    assert either.map(lambda x: x + 1).value == 1


def test_is_either():
    either = Either(1)
    assert Either.is_either(either) == True


def test_is_not_either():
    assert Either.is_either(1) == False
