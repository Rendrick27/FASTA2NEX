# FASTA to NEXUS Converter
## Description
This repository contains a script and associated unit tests for converting DNA sequence data from FASTA format to NEXUS format. The script `fasta2nex.py` consists of functions to read FASTA files, generate NEXUS headers, and convert the entire content into a NEXUS formatted output.

## Features `fasta2nex.py`
* read_fasta(file_path): Reads a FASTA file and returns a dictionary of sequences;
* generate_nexus_header(sequences): Generates a NEXUS header and MATRIX block from a dictionary of sequences;
* fasta_to_nexus(file_path): Converts a FASTA file to NEXUS format and prints the output to STDOUT.

## Features `script_test.py`
This script contains unit tests for the functions provided in `fasta2nex.py`. It ensures that each function works correctly by checking them against expected outputs using the `unittest` framework.

## Requirements
* <a href= "https://www.python.org/"> Python </a> 

## Installation
```bash
# Download the project
wget https://github.com/Rendrick27/FASTA2NEX/archive/refs/heads/main.zip

# Unzip the folder
unzip main.zip
```
## Usage
```bash
cd main.zip
```
Then, run the following command:
```bash
python fasta2nex.py input.fasta
```

* Replace input.fasta with the path to your FASTA file.

* The NEXUS output will be printed to the console

To run the `script_test.py`:

```bash
python -m unittest script_test.py
```
## Motivation
* Practical Application: To provide a simple and efficient way to convert DNA sequence data from the widely used FASTA format to the NEXUS format, which is commonly used in phylogenetic analysis;

* Educational: This script was developed as a homework assignment for UC Análise de Sequências Biológicas. 

## Credits
<p> <a href= "https://github.com/Rendrick27"> Rendrick Carreira - 201901365 </a> </p>
<p> <a href= "https://github.com/StarGazerNex"> Ravi Silva - 202100191 </a> </p>
<p> <a href= "https://github.com/Francisca-Figueiredo"> Francisca Figueiredo  - 202200580 </a> </p>

## License
GPLv3