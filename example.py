from settipy import settipy

if __name__ == "__main__":
    # setting strings

    settipy.set(
        flag_name="FOOBAR",
        default="default_value_for_foo_bar",
        message="explain why something is foobar"
    )

    # setting integers
    settipy.set_int("answer_to_the_universe", 42, "explain why 42 is the answer to the universe")

    # setting Booleans
    settipy.set_bool("hamlet", True, "to be or not to be?")

    # setting list
    # setting sep value is not needed defaults to ",".
    # settipy.set_list("abc", ["a", "b", "c"], "list of abc")

    # cli equivalent `-abc a.b.c`
    settipy.set_list("abc", ["a", "b", "c"], "list of abc", sep=".")

    # Values that should be set by vars
    # settipy.set_bool("foshure", True, "should be set by cli or env", should=True)

    # Run parse after the setting set.
    settipy.parse()

    foobar = settipy.get("FOOBAR")

    print("foobar =", foobar)
    print("answer to the universe =", settipy.get("answer_to_the_universe"))
    print("to be or not to be? =", settipy.get("hamlet"))
    print("list of abc", settipy.get("abc"))

# $ python3 example.py --help
# usage of example.py
# 	-FOOBAR str - default: default_value_for_foo_bar
# 		explain why something is foobar
# 	-answer_to_the_universe int - default: 42
# 		explain why 42 is the answer to the universe
# 	-hamlet bool - default: True
# 		to be or not to be?
# 	-abc list - default: ['a', 'b', 'c']
# 		list of abc
