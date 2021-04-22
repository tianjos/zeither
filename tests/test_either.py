from zeither import Either, left, right


def test_either_map():
    either = right(1)
    assert either.map(lambda x: x + 1).value == 2


def test_either_map_left_side():
    either = left(1)
    assert either.map(lambda x: x + 1).value == 1


def test_left_map():
    either = left(1)
    assert either.left_map(lambda x: x + 1).value == 2


def test_left_map_right_side():
    either = right(1)
    assert either.left_map(lambda x: x + 1).value == 1


def test_is_either():
    either = Either(1)
    assert Either.is_either(either) == True


def test_is_not_either():
    assert Either.is_either(1) == False


def test_is_right():
    either = right(1)
    assert either.is_right == True


def test_is_not_right():
    either = left(1)
    assert either.is_right == False


def test_bind():
    either = right(1)
    assert Either.is_either(either.bind(lambda n: right(n + 1))) == True


def test_bind_value():
    either = right(1)
    assert either.bind(lambda n: right(n + 1)).value == 2


def test_bind_left_side():
    either = left(1)
    assert Either.is_either(either.bind(lambda n: right(n + 1))) == True


def test_bind_value_left_side():
    either = left(1)
    assert either.bind(lambda n: right(n + 1)).value == 1