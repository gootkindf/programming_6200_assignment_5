"""
This Module is used for configuration, first its starts with error printing
"""

# Error": doesn't conform to snake_case naming style
# pylint: disable=invalid-name

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_error_string_4_ValueError():
    """
    Print invalid argument message for ValueError
    """
    print('Invalid argument Value for opening for reading')


def get_error_string_4_TypeError():
    """
    Print invalid argument message for TypeError
    """
    print("Invalid argument Type passed in")


def get_error_string_4_opening_file_OSError(file=None, mode=None):
    """
    Print invalid argument message for OSError
    :param file: The file name
    :param mode: Mode to open file in
    """
    print(f'Could not open file (os error): {file} with mode {mode}')


def get_unigene_directory():
    """
    Returns the data from the unigene directory.
    :return: Unigene directory name
    """
    return _UNIGENE_DIR


def get_unigene_extension():
    """
    Returns the UNIGENE_FILE_ENDING variable for use in main program.
    :return: extension for unigene files
    """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
    Creates a dictionary of possible common names with scientific names.
    :return: Dictionary of conversions from different names.
    """
    homo_sapiens = 'Homo_sapiens'
    bos_taurus = 'Bos_taurus'
    equus_caballus = 'Equus_caballus'
    mus_musculus = 'Mus_musculus'
    ovis_aries = 'Ovis_aries'
    rattus_norvegicus = 'Rattus_norvegicus'
    host_keywords = {
        "bos taurus": bos_taurus,
        "cow": bos_taurus,
        "cows": bos_taurus,
        'equus caballus': equus_caballus,
        'horse': equus_caballus,
        'horses': equus_caballus,
        'homo sapiens': homo_sapiens,
        'human': homo_sapiens,
        'humans': homo_sapiens,
        'mus musculus': mus_musculus,
        'mouse': mus_musculus,
        'mice': mus_musculus,
        'ovis aries': ovis_aries,
        'sheep': ovis_aries,
        'sheeps': ovis_aries,
        'rattus norvegicus': rattus_norvegicus,
        'rat': rattus_norvegicus,
        'rats': rattus_norvegicus
    }

    return host_keywords
