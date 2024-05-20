import sys


def read_fasta(input_file):
    """
    Reads a FASTA file and returns a dictionary where each key is a sequence
    name and each value is the corresponding sequence.

    Args:
        input_file (str): The path to the input FASTA file.

    Returns:
        dict: A dictionary where each key is a sequence name and each value
        is the corresponding sequence.
    """

    def truncate_name(name):
        return name[:99]

    def normaliz_seq(sequence):
        return sequence.replace(".", "N").replace("-", "N")

    sequences = {}
    with open(input_file, "r") as f:
        sequence = ""
        name = None
        names_set = set()
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name is not None:
                    truncated_name = truncate_name(name)
                    if truncated_name in names_set:
                        raise ValueError(f"Same seq name:{truncated_name}")
                    sequences[truncated_name] = normaliz_seq(sequence.upper())
                    names_set.add(truncated_name)
                    sequence = ""
                name = line[1:]  # Remove the ">" character from the name
            else:
                sequence += line
        if name is not None:
            truncated_name = truncate_name(name)
            if truncated_name in names_set:
                raise ValueError(f"Duplicate sequence name: {truncated_name}")
            sequences[truncated_name] = normaliz_seq(sequence.upper())
            names_set.add(truncated_name)
    return sequences


def generate_nexus_header(sequences):
    """
    Generates the NEXUS DATA header and MATRIX block.

    Args:
        sequences (dict): A dictionary where each key is a sequence name
        and each value is the corresponding sequence.

    Returns:
        str: The NEXUS DATA header and MATRIX block.
    """
    n_tax = len(sequences)
    n_char = len(next(iter(sequences.values())))
    header = [
        "#NEXUS\n",
        "BEGIN DATA;",
        f"DIMENSIONS NTAX={n_tax} NCHAR={n_char};",
        "FORMAT DATATYPE=DNA GAP=- MISSING=N;",
        "MATRIX"
    ]
    matrix_lines = [f"{name} {sequence}" for name, sequence
                    in sequences.items()]
    matrix = "\n".join(matrix_lines) + "\n;\nEND;"
    return "\n".join(header) + "\n" + matrix


def fasta_to_nexus(input_file):
    """
    Converts a FASTA file to NEXUS format and prints it to stdout.

    Args:
        input_file (str): The path to the input FASTA file.
    """
    sequences = read_fasta(input_file)
    nexus_content = generate_nexus_header(sequences)
    print(nexus_content)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
        fasta_to_nexus(input_file)
    else:
        print("Usage: python FASTA2NEX.py input.fasta > output.nexus")
