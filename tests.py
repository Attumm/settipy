import os
import sys

import unittest
from unittest import mock

import importlib

import settipy


class TestFeatures(unittest.TestCase):
    """
    Took over the testing style from the official argparse.
    https://github.com/python/cpython/blob/main/Lib/test/test_argparse.py#L182
    """

    def setUp(self):
        importlib.reload(settipy)

    def tearDown(self):
        pass

    def test_happy_path_default(self):
        setpy = settipy.settipy

        expected = "default value for foobar"
        setpy.set(
            flag_name="FOOBAR",
            default=expected,
            message="explain why something is foobar"
        )
        setpy.parse()
        self.assertEqual(expected, setpy.get("FOOBAR"))

    def test_happy_path_get_pythonic(self):
        setpy = settipy.settipy

        expected = "default value for foobar"
        setpy.set(
            flag_name="FOOBAR",
            default=expected,
            message="explain why something is foobar"
        )
        setpy.parse()
        self.assertEqual(expected, setpy["FOOBAR"])

    def test_happy_path_env(self):
        setpy = settipy.settipy

        expected = "value set in env"
        patched_environ = {"FOOBAR": expected}

        with mock.patch.dict(os.environ, patched_environ, clear=True):
            setpy.set(
                flag_name="FOOBAR",
                default="default value for foobar",
                message="explain why something is foobar"
            )
            setpy.parse()
            self.assertEqual(expected, setpy.get("FOOBAR"))

    def test_happy_path_cli(self):
        setpy = settipy.settipy

        expected = "value_set_with_cli"

        patched_argv = ["./foo.py", "--FOOBAR", expected]
        with mock.patch.object(sys, "argv", patched_argv):
            setpy.set(
                flag_name="FOOBAR",
                default="default value for foobar",
                message="explain why something is foobar"
            )
            setpy.parse()
            self.assertEqual(expected, setpy.get("FOOBAR"))

    def test_happy_path_order_of_precedence_cli(self):
        setpy = settipy.settipy

        expected = "value_set_with_cli"
        not_expected = "value_set_with_env"
        patched_argv = ["./foo.py", "--FOOBAR", expected]
        patched_environ = {"FOOBAR": not_expected}

        with mock.patch.dict(os.environ, patched_environ, clear=True):
            with mock.patch.object(sys, "argv", patched_argv):
                setpy.set(
                    flag_name="FOOBAR",
                    default="default value for foobar",
                    message="explain why something is foobar"
                )
                setpy.parse()
                self.assertEqual(expected, setpy.get("FOOBAR"))

    def test_happy_path_order_of_precedence_switched_mocking(self):
        setpy = settipy.settipy

        expected = "value_set_with_cli"
        not_expected = "value_set_with_env"
        patched_argv = ["./foo.py", "--FOOBAR", expected]
        patched_environ = {"FOOBAR": not_expected}

        with mock.patch.object(sys, "argv", patched_argv):
            with mock.patch.dict(os.environ, patched_environ, clear=True):
                setpy.set(
                    flag_name="FOOBAR",
                    default="default value for foobar",
                    message="explain why something is foobar"
                )
                setpy.parse()
                self.assertEqual(expected, setpy.get("FOOBAR"))

    def test_var_not_set(self):
        setpy = settipy.settipy

        cli_value = "value_set_with_cli"
        env_value = "value_set_with_env"
        patched_argv = ["./foo.py", "--FOOBAR", cli_value]
        patched_environ = {"FOOBAR": env_value}

        flag_name = "DOENST_EXIT"

        with mock.patch.object(sys, "argv", patched_argv):
            with mock.patch.dict(os.environ, patched_environ, clear=True):
                setpy.set(
                    flag_name="FOOBAR",
                    default="default value for foobar",
                    message="explain why something is foobar"
                )
                setpy.parse()

                with self.assertRaises(KeyError):
                    setpy.get(flag_name)

    def test_var_should_be_set(self):
        setpy = settipy.settipy
        setpy.test_mode = True

        cli_value = "value_set_with_cli"
        env_value = "value_set_with_env"
        patched_argv = ["./foo.py", "--FOOBAR", cli_value]
        patched_environ = {"FOOBAR": env_value}

        flag_name = "DOENST_EXIT"
        with mock.patch.object(sys, "argv", patched_argv):
            with mock.patch.dict(os.environ, patched_environ, clear=True):
                setpy.set(
                    flag_name=flag_name,
                    default="default value for foobar",
                    message="explain why something is foobar",
                    should=True
                )

                with self.assertRaises(Exception):
                    setpy.parse()

    def test_var_should_be_of_options(self):
        setpy = settipy.settipy
        setpy.test_mode = True

        cli_value = "value_set_env"
        env_value = "value_set_with_env"
        patched_argv = ["./foo.py", "--FOOBAR", cli_value]
        patched_environ = {"FOOBAR": env_value}

        flag_name = "FOOBAR"
        with mock.patch.object(sys, "argv", patched_argv):
            with mock.patch.dict(os.environ, patched_environ, clear=True):
                setpy.set(
                    flag_name=flag_name,
                    default="default value for foobar",
                    message="explain why something is foobar",
                    options=["foo", "bar"],
                )

                with self.assertRaises(Exception):
                    setpy.parse()


if __name__ == '__main__':
    unittest.main()
