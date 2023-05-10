import sys

def read_fasta(input_file):
    """
    Reads a FASTA file and returns a dictionary where each key is a sequence name
    and each value is the corresponding sequence.
    
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
    """
    Writes the sequences in NEXUS format to stdout, with a MrBayes block including the
    provided ngen and outgroup parameters.
    
    Args:
        sequences (dict): A dictionary where each key is a sequence name and each value
        is the corresponding sequence.
        ngen (int): The number of generations to run in the MrBayes analysis.
        outgroup (str): The name of the outgroup sequence.
    """
    print("#NEXUS")
    print("begin data;")
    print("dimensions ntax={} nchar={};".format(len(sequences), len(next(iter(sequences.values())))))
    print("format datatype=DNA gap=- missing=N;")
    print("matrix")
    
    for name, sequence in sequences.items():
        print("{} {}".format(name, sequence))
    print(";")
    print("end;")
    print("begin mrbayes;")
    print("set autoclose=yes nowarn=yes;")
    print("lset nst=6 rates=gamma;")
    print("mcmc ngen={} samplefreq=100 diagnfreq=1000 burninfrac=0.25 starttree=random;".format(ngen))
    if outgroup is not None:
        print("outgroup {};".format(outgroup))
    print("end;")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        sequences = read_fasta(input_file)
        write_nexus(sequences)
    else:
        print("Usage: python FASTA2NEX.py input.fasta > output.nexus")