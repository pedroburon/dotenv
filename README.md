Python Dot Env Handler
======================

Shell Command and Library to write and read `.env` like files.

[![Latest Version](https://pypip.in/version/dotenv/badge.svg)](https://pypi.python.org/pypi/dotenv/)
[![Build Status](https://travis-ci.org/pedroburon/dotenv.svg?branch=master)](https://travis-ci.org/pedroburon/dotenv)
[![Coverage Status](https://coveralls.io/repos/pedroburon/dotenv/badge.svg)](https://coveralls.io/r/pedroburon/dotenv)

`.env` files are commonly used with `Procfile`-based apps.

Usage
-----

### Shell

Inspect file

```shell
$ dotenv
FOO: bar
Bar: baz
```

Get value for key

```shell
$ dotenv FOO
FOO: bar
```

Set value for key

```shell
$ dotenv FOO baz
FOO: baz
```

### As a library

```python
>>> from dotenv import Dotenv
>>> dotenv = DotEnv('/path/to/.env')
>>> print dotenv
{"FOO": "bar", "Bar": "baz"}
>>> dotenv['FOO']
"bar"
>>> dotenv['FOO'] = "baz"
>>> dotenv['FOO']
"baz"
>>> del dotenv['FOO']
>>> print dotenv
{"Bar": "baz"}
```

> Every action is persisted.


### Use with Django

```python
# add this to manage.py above `execute_from_command_line(sys.argv)`

from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), '.env'))
os.environ.update(dotenv)

```