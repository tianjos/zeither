# Zeither

Either Monad only for study purposes now.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install zeither
```

## Usage

```python
from zeither import Either

either = Either(1)

assert either.map(lambda n: n + 1).value == 2
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)