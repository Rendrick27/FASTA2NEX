import sys
import unittest
from io import StringIO
from fasta2nex import read_fasta, generate_nexus_header, fasta_to_nexus


class testfasta2nex(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by creating a fake FASTA file and defining
        expected outputs for the tests.
        """
        self.fasta_content = """
>seq1
ACGTACGT
>seq2
TGCA-TGC
"""
        self.fasta_file = "test.fasta"

        with open(self.fasta_file, "w") as f:
            f.write(self.fasta_content)

        self.expected_sequences = {
            "seq1": "ACGTACGT",
            "seq2": "TGCANTGC"
        }

        self.expected_nexus_header = """#NEXUS

BEGIN DATA;
DIMENSIONS NTAX=2 NCHAR=8;
FORMAT DATATYPE=DNA GAP=- MISSING=N;
MATRIX
seq1 ACGTACGT
seq2 TGCANTGC
;
END;"""

    def test_read_fasta(self):
        """
        Test if the read_fasta function correctly reads the FASTA file and
        returns the expected dictionary of sequences.
        """
        result = read_fasta(self.fasta_file)
        self.assertEqual(result, self.expected_sequences)

    def test_generate_nexus_header(self):
        """
        Test if the generate_nexus_header function generates the correct NEXUS
        header and MATRIX block from the given sequences dictionary.
        """
        result = generate_nexus_header(self.expected_sequences)
        self.assertEqual(result, self.expected_nexus_header)

    def test_fasta_to_nexus(self):
        """
        Test if the fasta_to_nexus function prints the correct NEXUS format
        to stdout.
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        fasta_to_nexus(self.fasta_file)
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected NEXUS header and matrix
        self.assertEqual(captured_output.getvalue().strip(),
                         self.expected_nexus_header)
