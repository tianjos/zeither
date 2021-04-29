# Zeither

Either Monad only for study purposes now.

## Installation

Use the package manager [pip](https://pypi.org/project/zeither/) to install zeither.

```bash
pip install zeither
```

## Usage

```python
from zeither import Either, left, right, is_either

either = Either(1)

assert either.map(lambda n: n + 1).value == 2

either = right('foo')

assert either.map(lambda prefix: prefix + 'bar').value == 'foobar'

either = left(ValueError('exception'))

assert either.left_map(lambda error: True if isinstance(error, ValueError) else False).value == True

either = right(1)

assert either.bind(lambda n: right(n + 1)).value == 2

either = left(1)

assert either.bind(lambda n: right(n + 1)).value == 1

assert is_either(either) == True

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)