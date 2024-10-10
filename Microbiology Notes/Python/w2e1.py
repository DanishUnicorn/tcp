# With this template, you can replicate a DNA sequence, identify the Pribnow box and -35 region, transcribe the DNA sequence to mRNA, and translate the mRNA sequence into amino acids. The only thing needed is to insert your template strand and primer sequence, and the program will do the rest. xD


# ------------------------------------------ Replicating the Template Strand ------------------------------------------
template_strand = "GATTAGGTAACTGTGATTCGTACGTAACGTGACGATATTAGCATCCACCGCATACAGACGATATGCATAGCTGATCATATCGCC"
primer = "AUCCAUU"

# Substitute "U" with "T" in the primer
if "U" in primer:
    primer = primer.replace("U", "T")

# Find the complementary sequence of the primer on the template strand
complementary_primer = "".join([{"A": "T", "C": "G", "G": "C", "T": "A"}[base] for base in primer][::-1])

# Find the location of the complementary sequence on the template strand
start_index = template_strand.find(complementary_primer[::-1])

# Create the replicated strand by taking the complementary sequence of the template strand starting from the primer
replicated_strand = "".join([{"A": "T", "C": "G", "G": "C", "T": "A"}[base] for base in template_strand[start_index:]])

print("Replicated DNA sequence:", replicated_strand)

# ------------------------------------------ Identifying Pribnow box & -35 region ------------------------------------------
pribnow_box = "TATAAT"
minus_35_region = "TTGACA"

pribnow_index = replicated_strand.find(pribnow_box)
minus_35_index = replicated_strand.find(minus_35_region)

print("Pribnow box(-10):", pribnow_index)
print("(-35) region:", minus_35_index)

# ------------------------------------------ Transcribing to mRNA ------------------------------------------
transcription_start_index = pribnow_index + len(pribnow_box) + 10

mRNA = "".join([{"T": "U"}[base] if base in "T" else base for base in replicated_strand[transcription_start_index:]])

print("mRNA:", mRNA)

# ------------------------------------------ Translating mRNA into Amino Acids ------------------------------------------
codon_table = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "fMet",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

# Find the start codon
start_index = mRNA.find("AUG")

# Translate the mRNA sequence if start codon is found
if start_index != -1:
    # Translate the mRNA sequence
    amino_acids = []
    for i in range(start_index, len(mRNA), 3):
        codon = mRNA[i:i+3]
        amino_acid = codon_table.get(codon, "Unknown")
        if amino_acid == "Stop":
            break
        amino_acids.append(amino_acid)

    print("Amino Acids:", "-".join(amino_acids))
else:
    print("No start codon found.")