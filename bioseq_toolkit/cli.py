"""Command-line interface for BioSeq Toolkit."""

import argparse
import csv
from pathlib import Path

from bioseq_toolkit.fasta_parser import read_fasta
from bioseq_toolkit.sequence_utils import summarize_sequence


def print_summary(summary: dict) -> None:
    """Print sequence summary in a readable terminal format."""
    print("=" * 60)
    print(f"Sequence ID: {summary['sequence_id']}")
    print(f"Length: {summary['length_bp']} bp")
    print(f"Base counts: {summary['base_counts']}")
    print(f"GC content: {summary['gc_content_percent']}%")
    print(f"RNA transcript: {summary['rna_transcript']}")
    print(f"Reverse complement: {summary['reverse_complement']}")

    if "motif" in summary:
        positions = summary["motif_positions"]
        print(f"Motif searched: {summary['motif']}")
        print(f"Motif positions: {positions if positions else 'Not found'}")


def export_csv(summaries: list[dict], output_path: str | Path) -> None:
    """Export sequence summaries to a CSV file."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "sequence_id",
        "length_bp",
        "gc_content_percent",
        "A",
        "T",
        "G",
        "C",
        "N",
        "motif",
        "motif_positions",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for summary in summaries:
            base_counts = summary["base_counts"]
            row = {
                "sequence_id": summary["sequence_id"],
                "length_bp": summary["length_bp"],
                "gc_content_percent": summary["gc_content_percent"],
                "A": base_counts["A"],
                "T": base_counts["T"],
                "G": base_counts["G"],
                "C": base_counts["C"],
                "N": base_counts["N"],
                "motif": summary.get("motif", ""),
                "motif_positions": ";".join(map(str, summary.get("motif_positions", []))),
            }
            writer.writerow(row)


def analyze_fasta(file_path: str, motif: str | None = None, output: str | None = None) -> None:
    """Analyze all sequences in a FASTA file."""
    sequences = read_fasta(file_path)

    if not sequences:
        print("No sequences were found in the FASTA file.")
        return

    summaries = []

    for sequence_id, sequence in sequences.items():
        summary = summarize_sequence(sequence_id, sequence, motif)
        summaries.append(summary)
        print_summary(summary)

    if output:
        export_csv(summaries, output)
        print("=" * 60)
        print(f"CSV results saved to: {output}")


def main() -> None:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(
        description="Analyze DNA sequences from a FASTA file."
    )

    parser.add_argument(
        "fasta_file",
        help="Path to the FASTA file to analyze."
    )

    parser.add_argument(
        "--motif",
        help="Optional DNA motif to search for."
    )

    parser.add_argument(
        "--output",
        help="Optional CSV file path for saving results."
    )

    args = parser.parse_args()
    analyze_fasta(args.fasta_file, args.motif, args.output)


if __name__ == "__main__":
    main()
