# BioSeq Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Project](https://img.shields.io/badge/Portfolio-Bioinformatics-purple)

BioSeq Toolkit is a beginner-friendly Python project for basic DNA sequence analysis.

This is **Project 1** in my bioinformatics portfolio series. The purpose is to build a strong foundation in sequence handling before moving into larger FASTA datasets, NCBI data retrieval, restriction enzyme analysis, and sequence alignment.

## Why I Built This

Most bioinformatics workflows begin with biological sequence data. Before analyzing large public datasets, I wanted to understand the core operations used on DNA sequences:

- cleaning sequence input
- checking sequence validity
- calculating base composition
- calculating GC content
- converting DNA to RNA
- finding reverse complements
- searching for DNA motifs
- reading FASTA files

The project is intentionally simple, but the structure is written like a real reusable Python tool.

## Features

| Feature | Description |
|---|---|
| Base counting | Counts A, T, G, C and N bases |
| GC content | Calculates GC percentage |
| DNA validation | Checks for invalid characters |
| Transcription | Converts DNA to RNA |
| Reverse complement | Produces the reverse complement strand |
| Motif search | Finds all motif locations using 1-based indexing |
| FASTA parser | Reads one or more sequences from FASTA files |
| Command-line interface | Runs analysis directly from the terminal |
| CSV export | Saves analysis results into a CSV file |

## Repository Structure

```text
bioinformatics-project-00-seqtool/
├── bioseq_toolkit/
│   ├── __init__.py
│   ├── sequence_utils.py
│   ├── fasta_parser.py
│   └── cli.py
├── examples/
│   ├── sample_sequence.fasta
│   └── BRCA1_fragment.fasta
├── results/
│   └── example_output.csv
├── tests/
│   ├── test_sequence_utils.py
│   └── test_fasta_parser.py
├── docs/
│   └── project_notes.md
├── .github/
│   └── workflows/
│       └── tests.yml
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/pankhilpandya01-star/bioinformatics-project-00-seqtool.git
cd bioinformatics-project-00-seqtool
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Run the Toolkit

Analyze the sample FASTA file:

```bash
python -m bioseq_toolkit.cli examples/sample_sequence.fasta
```

Search for a motif:

```bash
python -m bioseq_toolkit.cli examples/sample_sequence.fasta --motif ATG
```

Export results to CSV:

```bash
python -m bioseq_toolkit.cli examples/sample_sequence.fasta --motif ATG --output results/my_output.csv
```

## Example Output

```text
============================================================
Sequence ID: sample_dna_sequence
Length: 66 bp
Base counts: {'A': 15, 'T': 12, 'G': 20, 'C': 19, 'N': 0}
GC content: 59.09%
RNA transcript: AUGCGUACGUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAG
Reverse complement: CTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTACGTACGCAT
Motif searched: ATG
Motif positions: [1]
```

## Testing

Run tests with:

```bash
pytest
```

The repository also includes a GitHub Actions workflow that runs tests automatically when code is pushed.

## Skills Demonstrated

- Python functions and modules
- FASTA file parsing
- Command-line tools
- Unit testing with pytest
- CSV output
- GitHub repository organization
- Basic biological sequence analysis

## Limitations

This project does not perform advanced sequence alignment, gene annotation, or variant analysis. Those topics will be handled in later projects.

## Next Project

**Project 2: FASTA Explorer**

The next project will build on this toolkit by analyzing multiple sequences, comparing sequence statistics, calculating N50, and generating summary reports.

## Portfolio Series

1. **BioSeq Toolkit**
2. FASTA Explorer
3. NCBI Sequence Fetcher
4. Restriction Enzyme Analyzer
5. Sequence Comparison Toolkit
