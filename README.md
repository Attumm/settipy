# settipy
## _settings should be simple, and with settipy it is._

settings parses command line and environment variables on one line.
And makes it available throughout the code base. Making using settings in your project as boring and unimportant as it should be.
settings vars is as simple as:
```go
settipy.set("FOO", "default value", "help text")
```
getting vars out has the same level of complexity as setting the value.
```go
settipy["FOO"]
```


## Features
- Simple to use
- supports command line and environment variables
- Support for types: str, int, bool, list, dict
- Singleton, makes it easy to use in program anywhere in the code-base
- Supports help text with --help
- Ease of use in any environment examples: linux, docker, k8
- Force program to be run with env or cli vars.


## Example
example of how to use. More can be found in the [example_project](https://github.com/Attumm/settipy/blob/main/example.py)
```python
settipy.set("FOO", "default value", "handy help text")

settipy.parse()

print("foo = ", settipy["FOO"])
```
The above go will produce program that can be used as follows.
get handy help text set in the above example on the same line.
This can get very handy when the project grows and is used in different environments
```python
$ python example.py --help
Usage of example.py:
  -FOO string
      handy help text (default "default value")
```

When no value is given, default value is used
```python
$ python example.py
foo = default value
```

Running the binary with command line input
```python
$ python example.py -FOO bar
foo = bar
```
Running the binary with environment variable
```python
$ FOO=ok;python example.py
foo = ok
```

## Order of preference
variables are set with preference
variables on the command line will have highest preference.
This because while testing you might want to override environment
The priority order is as follows
1. Command line input
2. Environment variables 
3. Default values

## Types
settipy supports different types. It's possible to use the method "get".
But to be more clear to the reader of the code you can add the type e.g "get_bool".
```python
// string
settipy.set("FOO", "default", "help text")
settipy["FOO"]

// integer
settipy.set_int("FOO", 42, "help text")
settipy["FOO"]

// boolean
settipy.set_bool("FOO", True, "help text")
settipy["FOO"]

// list
settipy.set_list("FOO", [1, 2, 3], "help text", sep=".")
settipy["FOO"]

dic = {
   "foo": ["bar",],
   "foo1": ["bar1", "bar2"]
}
settipy.set_dict("foodict", dic, "dict with lists", item_sep=";", key_sep=";", sep=",")
settipy["foodict"]
```

## Var Should be set
settipy supports different types.
```python
// string
settipy.set("foshure", True, "handy message", should=True)
```

```$ python3 example.py --hamlet_too
flag: foshure handy message: should be set
```

## Print vars before startup
Either run the program with `--settipy-verbose` as cli argument or `settipy.parse(verbose=True)`

## Install
```sh
$ pip install settipy
```

## Future features

* Add support for passwords. Password can be stored as hashes. With salt and pepper. Pepper can be stored in envirnoment and the salt given
at the cli. This will allow for safer storing of passwords. Passwords are then just hashes in config. At runtime at the parse fase settipy will
use the salt and pepper to decrypt the password. Since this will properly use external package the major version upgrade is needed. 1.0 will be requirement free.
and 2.0 will start to use packages.
* Add Typing
* Use logging


## License

MIT


