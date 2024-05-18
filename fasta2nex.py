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
    Replaces '.' and '-' characters with 'N' to represent missing
        and gap characters.

    Args:
        sequence (str): The input sequence.

    Returns:
        str: The normalized sequence.
    """
    return sequence.replace(".", "N").replace("-", "N")


def read_fasta(input_file):
    """
    Reads a FASTA file and returns a dictionary where each key is a
        sequence name and each value is the corresponding sequence.

    Args:
        input_file (str): The path to the input FASTA file.

    Returns:
        dict: A dictionary where each key is a sequence name
        and each value is the corresponding sequence.
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
                        truncated_name = (truncate_name(name[:97]) +
                                          f"{name_counter:02d}")
                        name_counter += 1
                    sequences[truncated_name] = normalize_sequence(
                        sequence.upper())
                    sequence = ""
                name = line[1:]  # Remove the ">" character from the name
                names_set.add(name)
            else:
                sequence += line
        if name is not None:
            truncated_name = truncate_name(name)
            while truncated_name in names_set:
                truncated_name = (truncate_name(name[:97]) +
                                  f"{name_counter:02d}")
                name_counter += 1
            sequences[truncated_name] = normalize_sequence(sequence.upper())
    return sequences


def generate_nexus_header(sequences):
    """
    Generates the NEXUS DATA header.

    Args:
        sequences (dict): A dictionary where each key is a sequence name
        and each value is the corresponding sequence.

    Returns:
        str: The NEXUS DATA header.
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
    return "\n".join(header)


def generate_nexus_matrix(sequences):
    """
    Generates the NEXUS MATRIX block.

    Args:
        sequences (dict): A dictionary where each key is a sequence name
            and each value is the corresponding sequence.

    Returns:
        str: The NEXUS MATRIX block.
    """
    matrix_lines = [f"{name} {sequence}"
                    for name, sequence in sequences.items()]
    matrix = "\n".join(matrix_lines) + "\n;\nEND;\n"
    return matrix


def fasta_to_nexus(input_file):
    """
    Converts a FASTA file to NEXUS format and prints it to stdout.

    Args:
        input_file (str): The path to the input FASTA file.
    """
    sequences = read_fasta(input_file)
    header = generate_nexus_header(sequences)
    matrix = generate_nexus_matrix(sequences)
    print(header)
    print(matrix)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
        fasta_to_nexus(input_file)
    else:
        print("Usage: python script.py input.fasta")
