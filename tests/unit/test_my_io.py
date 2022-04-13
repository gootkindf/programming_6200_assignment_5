"""Test suite for module my_io.py"""

import os
import pytest
from assignment5 import my_io


FILE_2_TEST = 'test.txt'


# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103


def test_existing_get_fh_4_reading():
    """Checks to see if get_fh can open a file for reading"""
    _create_test_file(FILE_2_TEST)
    test_fh = my_io.get_fh(FILE_2_TEST, 'r')
    assert hasattr(test_fh, 'readline') is True, 'Cannot open for reading'
    test_fh.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    """Checks to see if get_fh can open a file for writing"""
    test_fh = my_io.get_fh(FILE_2_TEST, 'w')
    assert hasattr(test_fh, 'write') is True, 'Cannot open for writing'


def test_get_fh_4_OSError():
    """Checks to see if get_fh properly raises an OSError when appropriate"""
    with pytest.raises(OSError):
        my_io.get_fh('no_file.txt', 'r')


def test_get_fh_4_ValueError():
    """Checks to see if get_fh properly raises a ValueError when
    appropriate"""
    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        my_io.get_fh('no_file.txt', 'rrr')
    os.remove(FILE_2_TEST)


def test_get_fh_4_TypeError():
    """Checks to see if get_fh properly raises a TypeError when appropriate"""
    _create_test_file(FILE_2_TEST)
    with pytest.raises(TypeError):
        my_io.get_fh([], 'r')
    os.remove(FILE_2_TEST)


def _create_test_file(file):
    """Helper file used to create a .txt file for testing"""
    open(file, 'w').close()
