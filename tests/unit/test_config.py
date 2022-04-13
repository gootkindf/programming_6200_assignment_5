"""Test suite for config module"""


from assignment5 import config


# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore all "Function name "test_get_fh_4_OSError" doesn't conform to snake_case naming style"
# pylint: disable=C0103


def test_get_string_ValueError(capsys):
    """
    Tests whether a string prints in reaction to a ValueError
    """
    config.get_error_string_4_ValueError()
    out, err = capsys.readouterr()
    assert out == "Invalid argument Value for opening for reading\n"
    assert err == ""


def test_get_string_TypeError(capsys):
    """
    Tests whether a string prints in reaction to a TypeError
    """
    config.get_error_string_4_TypeError()
    out, err = capsys.readouterr()
    assert out == "Invalid argument Type passed in\n"
    assert err == ""


def test_get_string_OSError(capsys):
    """
    Tests whether a string is printed in reaction to an OSError
    """
    config.get_error_string_4_opening_file_OSError('no_file.txt', 'r')
    out, err = capsys.readouterr()
    assert out == "Could not open file (os error): no_file.txt with mode r\n"
    assert err == ""


def test_get_unigene_directory():
    """
    Tests to ensure that the program is looking for the right data directory
    """
    uni_dir = config.get_unigene_directory()
    assert uni_dir == '/data/PROGRAMMING/assignment5'


def test_get_unigene_extension():
    """
    Tests to ensure that the unigene extension is properly applied to the
    file output
    """
    unigene = config.get_unigene_extension()
    assert unigene == 'unigene'


def test_get_host_keywords():
    """
    Placeholder
    :return:
    """
    key_dic = config.get_host_keywords()
    assert isinstance(key_dic, dict)
