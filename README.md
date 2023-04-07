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
Settipy offers a range of convenient features to help manage configuration settings, such as environment variables and command-line arguments. Here are some of the main features provided by Settipy:

* Unified access to environment variables and command-line arguments: Settipy allows you to access and manage both environment variables and command-line arguments through a single, consistent interface, making it easier to work with these configuration settings.

* Default values and descriptions: Settipy allows you to define default values and descriptions for configuration settings, ensuring that your application always has a fallback value and making it easier for other developers to understand the purpose of each setting.

* Encrypted storage: Settipy provides a secure method for storing sensitive information such as passwords, using a secret splitting technique that divides the data into two separate parts. This method ensures that an attacker would need access to both the process arguments and environment variables to reconstruct the full password, reducing the risk of unauthorized access.

* Flexible parsing: Settipy can be used to parse a wide range of data types, including integers, floats, booleans, and strings. This makes it suitable for various use cases and simplifies the process of working with different types of configuration settings.

* Easy integration: Settipy is designed to be easy to integrate into your existing projects. Simply import the library and start using it to manage your configuration settings without any complex setup.

* Platform independence: Settipy is compatible with both Unix and Windows systems, ensuring that your configuration settings can be managed consistently across different platforms.


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

## Verbose mode
Run the variables that are set before your programs runs, this can help with debugging or in production.
It's possible to hide variables with setting `password=True`
Either run the program with `--settipy-verbose` as cli argument or `settipy.parse(verbose=True)`

## Encryption of passwords

Why use Settipy's encryption feature?

While dedicated security solutions such as Vault provide more comprehensive protection, they can time-consuming or to complex for simple app. This can lead to situations where security is neglected or postponed.
Settipy's encryption offers a significantly more secure method of storing sensitive information compared to storing it in plaintext. In some scenarios, this secret splitting technique can provide an adequate level of security, making it a practical and accessible choice for developers.
By dividing a password or other sensitive data into two separate parts, Settipy ensures that an attacker would need access to both the process arguments and environment variables to reconstruct the full password. This approach effectively reduces the risk of unauthorized access and presents a user-friendly solution for securing sensitive data in your application.

    No plaintext storage: Sensitive information is divided into separate parts, ensuring that no plaintext version of the data is stored in any file or memory location.
    Enhanced security: Storing parts of sensitive data in different locations makes it more difficult for attackers to access the full password or sensitive data, as they would need to compromise both the environment variables and command-line arguments.
    Simple and Fast to implement: As such


Run the following command to get a prompt for your password.
```python
 python3 settipy.py --settipy-mode generate
Password:

cli: wNn30Cp3tJPNVvm4OsNYUr42BjY0pRSm
env: a55aae783460f836f8d43c507e9190defc612a930fda9cfd4d

python3 settipy.py -settipy-mode decrypt -settipy-key wNn30Cp3tJPNVvm4OsNYUr42BjY0pRSm -settipy-input a55aae783460f836f8d43c507e9190defc612a930fda9cfd4d
```

Store the env value in your environment
```sh
export DBPASS=wNn30Cp3tJPNVvm4OsNYUr42BjY0pRSm
```

Run your application
```python
python main.py --DBPASS=wNn30Cp3tJPNVvm4OsNYUr42BjY0pRSm
```

Example of main below
```python
from settipy import settipy

settipy.set(
    flag_name="DBPASS",
    default="test pass",
    message="secret for the database",
    encrypted=True,
)

settipy.parse()

password = settipy.get_encrypted("DBPASS")
```

## Install
```sh
$ pip install settipy
```

## Future features

* Add Typing
* Use logging


## License

MIT


