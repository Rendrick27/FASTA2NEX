# FASTA to NEXUS Converter
## Description
This Python script converts a FASTA file to NEXUS format with a MrBayes block, providing a convenient way to process biological sequence data for further analysis.

## Features
* Reads a FASTA file and converts it to NEXUS format.
* Handles truncation of sequence names to 99 characters for compatibility.
* Replaces missing and gap characters with "N" for consistency.
* Supports customization of the number of generations (ngen) and outgroup sequence (outgroup) for the MrBayes block.

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
python fasta2nex.py input.fasta [ngen] [outgroup]
```

* Replace input.fasta with the path to your FASTA file.

* Optionally, specify the number of generations (ngen) for the MrBayes analysis.

* Optionally, specify the name of the outgroup sequence (outgroup).

* The NEXUS output will be printed to the console

## Example
To convert a FASTA file named sequences.fasta to NEXUS format with 5000 generations and an outgroup sequence named outgroup1, run the following command:

`python fasta2nex.py sequences.fasta 5000 outgroup1`

## Credits
<p> <a href= "https://github.com/Rendrick27"> Rendrick Carreira - 201901365 </a> </p>
<p> <a href= "https://github.com/StarGazerNex"> Ravi Silva - 202100191 </a> </p>
<p> <a href= "https://github.com/Francisca-Figueiredo"> Francisca Figueiredo  - 202200580 </a> </p>

## License
GPLv3