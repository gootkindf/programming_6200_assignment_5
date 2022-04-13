# Assignment 5

This assignment is centered around a single program; gene_information_query.py. This program
accepts input in the form of a host argument and a gene argument, though it has default settings.
The program reads looks through a directory of host organisms, which in turn contain
unigene-formatted data files of different genes of interest. It then returns the tissues that the
gene of interest is found in.

## Description

This program looks through a directories of host organisms which in turn contain the
unigene-formatted files about different genes found in those host organisms. It accepts host and
gene arguments, but defaults to homo_sapiens and TGM1 respectively. The program parses the data in
the unigene file and prints a list of tissues in which the gene is expressed. In the event that 
the user enters a host organism that is not found it will print a list of possible hosts supported
by the program.

## Getting Started

### Dependencies

* Python 3

### Executing program

Call gene_information_query.py with or without a host and gene argument. Program defaults to 
homo_sapiens and TGM1.
```
python3 gene_information_query.py
python3 gene_information_query.py -host human -gene TGM1
python3 gene_information_query.py -host equus_caballus -gene API5
```

## Help

If you run into any problems, run the help command
```
python3 gene_information_query.py -h
```

## Authors
Fredrick Gootkind

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.
* https://gist.githubusercontent.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc/raw/d59043abbb123089ad6602aba571121b71d91d7f/README-Template.md_

Capturing output
* https://docs.pytest.org/en/6.2.x/capture.html