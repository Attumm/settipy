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
settipy.get("FOO")
```


## Features
- Simple to use
- supports command line and environment variables
- Support for types: str, int, bool
- Singleton, makes it easy to use in program anywhere in the code-base
- Supports help text with --help
- Ease of use in any environment examples: linux, docker, k8
- Force program to be run with env or cli vars.


## Example
example of how to use. More can be found in the [example_project](https://github.com/Attumm/settipy/blob/main/example.py)
```python
settipy.set("FOO", "default value", "handy help text")

settipy.parse()

print("foo = ", settipy.get("FOOBAR"))
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
settipy supports different types.
```python
// string
settipy.set("FOO", "default", "help text")
settipy.get("FOO")

// integer
settipy.set_int("FOO", 42, "help text")
settipy.get_int("FOO")

// boolean
settipy.set_bool("FOO", True, "help text")
settipy.get_bool("FOO")
```

## Var Should be set
settipy supports different types.
```python
// string
settipy.set("foshure", True, "handy message", should=True)
```

```$ python3 example.py --hamlet_too
flag: foshure should be set by cli or env: should be set
```

## Install
```sh
$ pip install settipy
```

## License

MIT


