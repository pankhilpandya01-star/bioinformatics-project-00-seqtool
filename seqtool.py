# BioSeq Toolkit
# Project 0: Simple DNA sequence analysis


def read_fasta(filename):
    sequence_id = ""
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                sequence_id = line.replace(">", "")
            else:
                sequence = sequence + line

    return sequence_id, sequence


def count_bases(sequence):
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    return a_count, t_count, g_count, c_count


def gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_total = g_count + c_count

    if len(sequence) == 0:
        return 0

    gc_percent = (gc_total / len(sequence)) * 100
    return round(gc_percent, 2)


def dna_to_rna(sequence):
    rna = sequence.replace("T", "U")
    return rna


def reverse_complement(sequence):
    complement = ""

    for base in sequence:
        if base == "A":
            complement = complement + "T"
        elif base == "T":
            complement = complement + "A"
        elif base == "G":
            complement = complement + "C"
        elif base == "C":
            complement = complement + "G"

    reverse = complement[::-1]
    return reverse


def find_motif(sequence, motif):
    positions = []
    motif_length = len(motif)

    for i in range(len(sequence) - motif_length + 1):
        if sequence[i:i + motif_length] == motif:
            positions.append(i + 1)

    return positions


# Main program
sequence_id, dna_sequence = read_fasta("example.fasta")
dna_sequence = dna_sequence.upper()

motif = "ATG"

a_count, t_count, g_count, c_count = count_bases(dna_sequence)

print("Sequence ID:", sequence_id)
print("DNA sequence:", dna_sequence)
print("Length:", len(dna_sequence))
print("A count:", a_count)
print("T count:", t_count)
print("G count:", g_count)
print("C count:", c_count)
print("GC content:", str(gc_content(dna_sequence)) + "%")
print("RNA sequence:", dna_to_rna(dna_sequence))
print("Reverse complement:", reverse_complement(dna_sequence))
print("Motif searched:", motif)
print("Motif positions:", find_motif(dna_sequence, motif))
