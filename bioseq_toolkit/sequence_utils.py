"""Utility functions for basic DNA and RNA sequence analysis."""

from collections import Counter


VALID_DNA_BASES = {"A", "T", "G", "C", "N"}


def clean_sequence(sequence: str) -> str:
    """Return an uppercase DNA sequence with whitespace removed."""
    if not isinstance(sequence, str):
        raise TypeError("Sequence must be provided as a string.")

    return (
        sequence.replace("\n", "")
        .replace("\r", "")
        .replace("\t", "")
        .replace(" ", "")
        .upper()
    )


def validate_dna(sequence: str) -> bool:
    """Return True when a sequence contains only valid DNA bases."""
    sequence = clean_sequence(sequence)
    return all(base in VALID_DNA_BASES for base in sequence)


def count_bases(sequence: str) -> dict[str, int]:
    """Count A, T, G, C and N bases in a DNA sequence."""
    sequence = clean_sequence(sequence)

    if not validate_dna(sequence):
        raise ValueError("Sequence contains invalid DNA characters.")

    counts = Counter(sequence)
    return {base: counts.get(base, 0) for base in ["A", "T", "G", "C", "N"]}


def gc_content(sequence: str) -> float:
    """Calculate GC content percentage for a DNA sequence."""
    sequence = clean_sequence(sequence)

    if not validate_dna(sequence):
        raise ValueError("Sequence contains invalid DNA characters.")

    if len(sequence) == 0:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")
    return round((gc_count / len(sequence)) * 100, 2)


def transcribe_dna_to_rna(sequence: str) -> str:
    """Convert DNA into RNA by replacing thymine with uracil."""
    sequence = clean_sequence(sequence)

    if not validate_dna(sequence):
        raise ValueError("Sequence contains invalid DNA characters.")

    return sequence.replace("T", "U")


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement of a DNA sequence."""
    sequence = clean_sequence(sequence)

    if not validate_dna(sequence):
        raise ValueError("Sequence contains invalid DNA characters.")

    complement_map = str.maketrans("ATGCN", "TACGN")
    return sequence.translate(complement_map)[::-1]


def find_motif(sequence: str, motif: str) -> list[int]:
    """Find all starting positions of a motif in a DNA sequence.

    Positions are returned using 1-based indexing, which is commonly used
    in biological sequence reporting.
    """
    sequence = clean_sequence(sequence)
    motif = clean_sequence(motif)

    if not motif:
        raise ValueError("Motif cannot be empty.")

    if not validate_dna(sequence) or not validate_dna(motif):
        raise ValueError("Sequence or motif contains invalid DNA characters.")

    positions = []
    motif_length = len(motif)

    for index in range(len(sequence) - motif_length + 1):
        if sequence[index:index + motif_length] == motif:
            positions.append(index + 1)

    return positions


def summarize_sequence(sequence_id: str, sequence: str, motif: str | None = None) -> dict:
    """Return a summary dictionary for a DNA sequence."""
    sequence = clean_sequence(sequence)

    summary = {
        "sequence_id": sequence_id,
        "length_bp": len(sequence),
        "gc_content_percent": gc_content(sequence),
        "base_counts": count_bases(sequence),
        "rna_transcript": transcribe_dna_to_rna(sequence),
        "reverse_complement": reverse_complement(sequence),
    }

    if motif:
        summary["motif"] = clean_sequence(motif)
        summary["motif_positions"] = find_motif(sequence, motif)

    return summary
