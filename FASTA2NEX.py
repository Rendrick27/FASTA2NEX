import sys

def read_fasta(input_file):
    sequences = {}
        with open(input_file, "r") as f:
            sequence = ""
            name = None
            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    if name is not None:
                        sequences[name] = sequence.upper()
                        sequence = ""
                    name = line[1:]
                    if len(name) > 99:
                        name = name[:99]
                else:
                    sequence += line.replace(".", "N").replace("-", "N").upper()
            if name is not None:
                sequences[name] = sequence.upper()
        return sequences

def write_nexus(sequences, ngen=10000, outgroup=None):
