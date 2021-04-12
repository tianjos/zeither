from zeither import __version__
from zeither import Either


def test_version():
    assert __version__ == "0.1.0"


def test_either_map():
    either = Either(1)
    assert either.map(lambda x: x + 1).value == 2