"""FASTA parser for BioSeq Toolkit."""

from pathlib import Path


def read_fasta(file_path: str | Path) -> dict[str, str]:
    """Read a FASTA file and return a dictionary of sequence_id: sequence."""
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"FASTA file not found: {file_path}")

    sequences: dict[str, str] = {}
    current_id: str | None = None
    current_sequence: list[str] = []

    with file_path.open("r", encoding="utf-8") as fasta_file:
        for line_number, line in enumerate(fasta_file, start=1):
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_sequence)

                current_id = line[1:].split()[0]
                current_sequence = []

                if not current_id:
                    raise ValueError(f"Missing FASTA sequence ID on line {line_number}.")
            else:
                if current_id is None:
                    raise ValueError("Invalid FASTA format. Sequence found before header.")
                current_sequence.append(line)

    if current_id is not None:
        sequences[current_id] = "".join(current_sequence)

    return sequences
