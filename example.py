from settipy import settipy

if __name__ == "__main__":
    # setting strings
    settipy.set("FOOBAR", "default_value_for_foo_bar", "explain why something is foobar")

    # setting integers
    settipy.set_int("answer_to_the_universe", 42, "explain why 42 is the answer to the universe")

    # setting Booleans
    settipy.set_bool("hamlet", True, "to be or not to be?")

    # Run parse after the setting set.
    settipy.parse()

    foobar = settipy.get("FOOBAR")

    print("foobar =", foobar)
    print("answer to the universe =", settipy.get_int("answer_to_the_universe"))
    print("to be or not to be? =", settipy.get_bool("hamlet"))

# $ python3 example.py --help
# usage of example.py
# 	-FOOBAR str - default: default_value_for_foo_bar
# 		explain why something is foobar
# 	-answer_to_the_universe int - default: 42
# 		explain why 42 is the answer to the universe
# 	-hamlet bool - default: True
# 		to be or not to be?
