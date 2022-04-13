"""
file    : gene_information_query.py
History : 4-Dec-2021

This script looks through a series of directories containing unigene files on
different genes organized by the species they were found in. By default the
program searches for the TGM1 gene in "Homo sapiens", but as written it can
accept the scientific or common names of 7 different species (cow, horse,
human, mouse, rat, sheep) in the following format (case insensitive):

1. "Homo sapiens"
2. homo_sapiens
3. human
4. humans

In instances where the host is not found, it returns a list of possible hosts
that could be searched for. In instances where the gene is not found, it
informs the user that the gene cannot be found in the directory of interest
and outputs a standard error.

Sample command for executing program:

python3 gene_information_query.py -host human -gene EXD1
"""

import sys
import os
import re
import argparse
from assignment5 import config
from assignment5 import my_io


def main():
    """Business logic"""
    args = get_args()
    temp_host = args[0]
    gene = args[1]
    host = modify_host_name(temp_host)
    file = os.path.join(config.get_unigene_directory(), host, gene + "." + config.get_unigene_extension())
    if my_io.is_valid_gene_file_name(file):
        # using f-strings
        print(f"\nFound Gene {gene} for {host.replace('_', ' ')}")
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {host.replace('_', ' ')}. exiting now...", file=sys.stderr)
        sys.exit(1)
    file_handle = my_io.get_fh(file, 'r')
    gene_data = get_gene_data(file_handle)
    print_output(host, gene, gene_data)
    file_handle.close()


def modify_host_name(host_name):
    """
    This function receives the host name as given in the command line,
    modifies the input into an acceptable form, and checks it against the list
    of possible hosts. If the host is found, it returns the host's scientific
    name as it appears in the host directory.
    :param host_name: The name of the host as given in the command line
    :return: The name of the host's gene directory as it appears in the host
    directory
    """
    name_list = config.get_host_keywords()
    host_name = host_name.casefold()
    host_name = host_name.replace('_', ' ')
    if host_name in name_list:
        host_file = name_list.get(host_name)
    else:
        _print_host_directories()
    return host_file


def _print_host_directories():
    """
    This script is executed in the event that the user puts in an unrecognized
    host organism. It prints a list of possible hosts by scientific name as
    well as a list of possible hosts by various common names.
    :return: None
    """
    name_list = config.get_host_keywords()
    sci_names = set()
    host_count = 1
    host_string = ''
    name_string = ''
    name_count = 1
    for key in name_list:
        sci_names.add(name_list[key])
    sci_list = list(sci_names)
    sci_list.sort()
    for s_n in sci_list:
        host_string += str('{:>2}. {}\n'.format(host_count, s_n))
        host_count += 1
    for name in name_list:
        name_string += ('{:>2}. {:<2}\n'.format(name_count, name.capitalize()))
        name_count += 1
    print(f'\n\nEither the Host Name your are searching for is not in the '
          'database\n\nor If you are trying to use the scientific name please'
          ' put the name in double quotes:\n\n"Scientific name"\n\nHere is a '
          '(non-case sensitive) list of available Hosts by scientific '
          f'name.\n\n{host_string}\nHere is a (non-case sensitive) list of '
          f'available Hosts by common name\n\n{name_string}', file=sys.stderr)
    sys.exit(1)


def get_gene_data(gene_file):
    """
    This function looks through the unigene file for a gene of interest given
    by the user at the command line. It isolates the section listing sites of
    expression and returns a list of the tissues in which the gene is
    expressed.
    :param gene_file: The opened Unigene file in read mode
    :return: a list of tissues found in the unigene file.
    """
    gene_text = gene_file.read()
    match = re.search('EXPRESS(.*)\n', gene_text)
    if match:
        tissue_strig = match.group(1)
        tissue_list = tissue_strig.split('|')
    for count, tissue in enumerate(tissue_list):
        tissue = tissue.strip(' ')
        tissue_list[count] = tissue
    tissue_list.sort()
    return tissue_list


def print_output(host, gene, express):
    """
    Prints an itemized output of the tissues in which the gene of interest is
    expressed in the host organism.
    :param host: the name of the host organism
    :param gene: the gene of interest
    :param express: the list of tissues in which the tissue is expressed
    :return: None
    """
    print(f'In {host.replace("_", " ")}, There are {len(express)} tissues that {gene} is '
          f'expressed in:\n')
    for count, tissue in enumerate(express):
        print('{:>2}. {}'.format(count + 1, tissue.capitalize()))


def get_args():
    """
    This function parses the arguments given in command line and returns
    the host and gene name or help menu
    :return: the host and gene of interest
    """
    parser = argparse.ArgumentParser(description='Give the Host and Gene '
                                                 'name')
    # Add arguments
    parser.add_argument('-host',
                        dest='host',
                        type=str,
                        help='Name of Host',
                        required=False,
                        default='Homo_sapiens')
    parser.add_argument('-gene',
                        dest='gene',
                        type=str,
                        help='Name of Gene',
                        required=False,
                        default='TGM1')
    query = [parser.parse_args().host, parser.parse_args().gene]
    return query


if __name__ == "__main__":
    main()
