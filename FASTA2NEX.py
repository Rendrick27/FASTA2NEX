import sys

def truncate_name(name):
    """
    Truncates a sequence name to 99 characters.

    Args:
        name (str): The sequence name.

    Returns:
        str: The truncated sequence name.
    """
    return name[:99]

def normalize_sequence(sequence):
    """
    Replaces '.' and '-' characters with 'N' to represent missing and gap characters.

    Args:
        sequence (str): The input sequence.

    Returns:
        str: The normalized sequence.
    """
    return sequence.replace(".", "N").replace("-", "N")

def read_fasta(input_file):
    """
    Reads a FASTA file and returns a dictionary where each key is a sequence name
    and each value is the corresponding sequence.

    If any sequence name is longer than 99 characters or there are two sequence names
    with the same first 99 characters, the names are truncated and appended with a
    two-digit number for uniqueness.

    Args:
        input_file (str): The path to the input FASTA file.

    Returns:
        dict: A dictionary where each key is a sequence name and each value is the
        corresponding sequence.
    """
    sequences = {}
    with open(input_file, "r") as f:
        sequence = ""
        name = None
        name_counter = 1  # Counter for appending numbers to truncated names
        names_set = set()  # Set to store truncated names and check uniqueness
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name is not None:
                    truncated_name = truncate_name(name)
                    while truncated_name in names_set:
                        truncated_name = truncate_name(name[:97]) + f"{name_counter:02d}"
                        name_counter += 1
                    sequences[truncated_name] = normalize_sequence(sequence.upper())
                    sequence = ""
                name = line[1:]  # Remove the ">" character from the name
                names_set.add(name)
            else:
                sequence += line
        if name is not None:
            truncated_name = truncate_name(name)
            while truncated_name in names_set:
                truncated_name = truncate_name(name[:97]) + f"{name_counter:02d}"
                name_counter += 1
            sequences[truncated_name] = normalize_sequence(sequence.upper())
    return sequences

def write_nexus(sequences, ngen=10000, outgroup=None):
    """
    Writes the sequences in NEXUS format to stdout, with a MrBayes block including the
    provided ngen and outgroup parameters.

    Args:
        sequences (dict): A dictionary where each key is a sequence name and each value
        is the corresponding sequence.
        ngen (int): The number of generations to run in the MrBayes analysis.
        outgroup (str): The name of the outgroup sequence.
    """
    print("#NEXUS\n")
    print("BEGIN DATA;")
    print("DIMENSIONS NTAX={} NCHAR={};".format(len(sequences), len(next(iter(sequences.values())))))
    print("FORMAT DATATYPE=DNA GAP=- MISSING=N;")
    print("MATRIX")

    for name, sequence in sequences.items():
        print("{} {}".format(name, sequence))
    print(";")
    print("END;\n")
    print("begin mrbayes;")
    print("  set autoclose=yes nowarn=yes;")
    print("  lset nst=6 rates=gamma;")
    print("  mcmc ngen={} samplefreq=100 diagnfreq=1000 burninfrac=0.25 starttree=random;".format(ngen))
    if outgroup is not None:
        print("  outgroup {};".format(outgroup))
    print("end;")

def fasta_to_nexus(input_file, ngen=10000, outgroup=None):
    """
    Converts a FASTA file to NEXUS format and prints it to stdout.

    Args:
        input_file (str): The path to the input FASTA file.
        ngen (int): The number of generations to run in the MrBayes analysis.
        outgroup (str): The name of the outgroup sequence.
    """
    sequences = read_fasta(input_file)
    write_nexus(sequences, ngen, outgroup)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]

        # Set default values for ngen and outgroup
        ngen = 10000
        outgroup = None

        # Check if ngen and outgroup arguments are provided
        if len(sys.argv) >= 4:
            ngen = int(sys.argv[2])
            outgroup = sys.argv[3]

        fasta_to_nexus(input_file, ngen, outgroup)
    else:
        print("Usage: python FASTA2NEX.py input.fasta [ngen] [outgroup] > output.nexus")
