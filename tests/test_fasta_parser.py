"""Tests for FASTA parser."""

from pathlib import Path

import pytest

from bioseq_toolkit.fasta_parser import read_fasta


def test_read_fasta(tmp_path: Path):
    fasta_file = tmp_path / "test.fasta"
    fasta_file.write_text(">seq1\nATGC\n>seq2\nGGCC\n", encoding="utf-8")

    sequences = read_fasta(fasta_file)

    assert sequences == {"seq1": "ATGC", "seq2": "GGCC"}


def test_missing_file_error():
    with pytest.raises(FileNotFoundError):
        read_fasta("missing_file.fasta")


def test_invalid_fasta_format(tmp_path: Path):
    fasta_file = tmp_path / "bad.fasta"
    fasta_file.write_text("ATGC\n>seq1\nATGC", encoding="utf-8")

    with pytest.raises(ValueError):
        read_fasta(fasta_file)
