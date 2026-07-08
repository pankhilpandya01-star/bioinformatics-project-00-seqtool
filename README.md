# BioSeq Toolkit

BioSeq Toolkit is my first beginner bioinformatics project. It is a simple Python program that analyzes DNA sequences from a FASTA file.

The goal of this project is not to make an advanced tool. The goal is to practice the basics of Python and bioinformatics in a way that I can understand and explain clearly.

## What This Project Does

The program can:

- read a FASTA file
- count A, T, G, and C bases
- calculate GC content
- convert DNA to RNA
- find the reverse complement
- search for a small DNA motif

## Files in This Project

```text
bioinformatics-project-00-seqtool/
├── seqtool.py
├── example.fasta
├── notes.md
├── README.md
├── requirements.txt
└── LICENSE
```

## How to Run

Open the project folder in the terminal and run:

```bash
python seqtool.py
```

The program uses the example FASTA file included in this repository:

```text
example.fasta
```

## Example Input

```text
>sample_sequence
ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAG
```

## Example Output

```text
Sequence ID: sample_sequence
DNA sequence: ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAG
Length: 35
A count: 7
T count: 8
G count: 11
C count: 9
GC content: 57.14%
RNA sequence: AUGCGUACGUAGCUAGCUAGCUAGCUAGCUAG
Reverse complement: CTAGCTAGCTAGCTAGCTAGCTACGTACGCAT
Motif searched: ATG
Motif positions: [1]
```

## What I Learned

While making this project, I practiced:

- writing basic Python functions
- using strings in Python
- reading a text file
- working with DNA sequence data
- calculating simple biological statistics
- organizing a small GitHub project

## Why This Project Matters

Most bioinformatics work starts with biological sequence data. This project helped me understand the basic operations that are used before moving into larger datasets and more advanced tools.

## Next Step

The next project will build on this by analyzing multiple FASTA sequences and creating a simple summary table.
