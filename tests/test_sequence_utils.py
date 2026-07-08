"""Tests for sequence utility functions."""

import pytest

from bioseq_toolkit.sequence_utils import (
    clean_sequence,
    validate_dna,
    count_bases,
    gc_content,
    transcribe_dna_to_rna,
    reverse_complement,
    find_motif,
    summarize_sequence,
)


def test_clean_sequence():
    assert clean_sequence("atgc\n atgc\t") == "ATGCATGC"


def test_validate_dna():
    assert validate_dna("ATGCN") is True
    assert validate_dna("ATGB") is False


def test_count_bases():
    assert count_bases("AATTGGCCN") == {"A": 2, "T": 2, "G": 2, "C": 2, "N": 1}


def test_gc_content():
    assert gc_content("AATTGGCC") == 50.0


def test_gc_content_empty_sequence():
    assert gc_content("") == 0.0


def test_transcribe_dna_to_rna():
    assert transcribe_dna_to_rna("ATGC") == "AUGC"


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_find_motif():
    assert find_motif("ATGCGCATGC", "ATG") == [1, 7]


def test_find_overlapping_motif():
    assert find_motif("AAAA", "AA") == [1, 2, 3]


def test_empty_motif_error():
    with pytest.raises(ValueError):
        find_motif("ATGC", "")


def test_invalid_sequence_error():
    with pytest.raises(ValueError):
        count_bases("ATBX")


def test_summarize_sequence():
    summary = summarize_sequence("seq1", "ATGC", "ATG")
    assert summary["sequence_id"] == "seq1"
    assert summary["length_bp"] == 4
    assert summary["gc_content_percent"] == 50.0
    assert summary["motif_positions"] == [1]
