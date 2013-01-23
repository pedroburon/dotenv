Python Dot Env Handler
======================

Shell Command and Library to write and read .env like files.

.env file are commonly used with Procfile based apps.

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
>>> from dotenv import DotEnv
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