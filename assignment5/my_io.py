"""
file    : my_io.py
History : 1-Dec-2021

This stores two functions for use in assignment 5 used to open file handles
and check to ensure that a file exists.
"""


import os
from assignment5 import config


def get_fh(file=None, mode=None):
    """
    filehandle : get_fh(infile, "r")
    This function takes 2 arguments; file name and mode i.e. what is needed to
    be done with this file. This function opens the file based on the modepassed in
    the argument and returns filehandle.
    @:param file: The file to open for the mode
    @:param mode: They way to open the file, e.g. reading, writing, etc
    @return: filehandle
    """

    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        config.get_error_string_4_opening_file_OSError(file, mode)
        raise
    except ValueError:
        config.get_error_string_4_ValueError()
        raise
    except TypeError:
        config.get_error_string_4_TypeError()
        raise


def is_valid_gene_file_name(file_name):
    """
    Checks to see if a file by the name given exists
    :param file_name: name of the file of interest
    :return: True if exists, False if not
    """
    return os.path.exists(file_name)
