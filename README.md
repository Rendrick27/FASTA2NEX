# FASTA to NEXUS Converter

This Python script converts a FASTA file to NEXUS format with a MrBayes block, providing a convenient way to process biological sequence data for further analysis.

## Features
* Reads a FASTA file and converts it to NEXUS format.
* Handles truncation of sequence names to 99 characters for compatibility.
* Replaces missing and gap characters with "N" for consistency.
* Supports customization of the number of generations (ngen) and outgroup sequence (outgroup) for the MrBayes block.

## Requirements
Python 3.x

1-Ensure you have Python 3.x installed on your system.

2-Download or clone the repository.

3-Open a terminal or command prompt and navigate to the repository's directory.

4-Run the following command:

`python FASTA2NEX.py input.fasta [ngen] [outgroup] > output.nexus`

* Replace input.fasta with the path to your FASTA file.

* Optionally, specify the number of generations (ngen) for the MrBayes analysis.

* Optionally, specify the name of the outgroup sequence (outgroup).

* The NEXUS output will be printed to the console, so redirect it to a file using > output.nexus.

## Example
To convert a FASTA file named sequences.fasta to NEXUS format with 5000 generations and an outgroup sequence named outgroup1, run the following command:

`python FASTA2NEX.py sequences.fasta 5000 outgroup1 > output.nexus`
