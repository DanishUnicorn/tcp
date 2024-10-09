# ---------------------------- DNA Replication, Transcription, and Translation ----------------------------

# ---------------------------- Definitions ----------------------------

# Define the start codon
start_codon = 'AUG'

# Define complementary base pairs for DNA replication
dna_base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

# Define RNA base pairs for transcription
rna_base_pairs = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}

# Define the Pribnow box (-10 region)
def find_pribnow_box(dna_sequence):
    pribnow_box = 'TATAAT'
    for i in range(len(dna_sequence) - len(pribnow_box) + 1):
        if dna_sequence[i:i+len(pribnow_box)] == pribnow_box:
            return dna_sequence[i:i+len(pribnow_box)], i
    return None, None

# Define the -35 region
def find_minus_35_region(dna_sequence):
    minus_35_region = 'TTGACA'
    for i in range(len(dna_sequence) - len(minus_35_region) + 1):
        if dna_sequence[i:i+len(minus_35_region)] == minus_35_region:
            return dna_sequence[i:i+len(minus_35_region)], i
    return None, None

# Define the RNA codon table for translation with three-letter amino acid names
RNAcodon_table = {
    'AUA': 'Ile', 'AUC': 'Ile', 'AUU': 'Ile', 'AUG': 'Met',
    'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACU': 'Thr',
    'AAC': 'Asn', 'AAU': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGC': 'Ser', 'AGT': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'CUA': 'Leu', 'CUC': 'Leu', 'CUG': 'Leu', 'CUU': 'Leu',
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCU': 'Pro',
    'CAC': 'His', 'CAU': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGU': 'Arg',
    'GUA': 'Val', 'GUC': 'Val', 'GUG': 'Val', 'GUU': 'Val',
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCU': 'Ala',
    'GAC': 'Asp', 'GAU': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGU': 'Gly',
    'UCA': 'Ser', 'UCC': 'Ser', 'UCG': 'Ser', 'UCU': 'Ser',
    'UUC': 'Phe', 'UUU': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UAC': 'Tyr', 'UAU': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGC': 'Cys', 'UGU': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp'
}

# Define the start codon
start_codon = 'AUG'

# Define complementary base pairs
base_pairs = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

# Define the DNA codon table for transcription with three-letter amino acid names
DNAcodon_table = {
    'ATA':'Ile', 'ATC':'Ile', 'ATT':'Ile', 'ATG':'Met',
    'ACA':'Thr', 'ACC':'Thr', 'ACG':'Thr', 'ACT':'Thr',
    'AAC':'Asn', 'AAT':'Asn', 'AAA':'Lys', 'AAG':'Lys',
    'AGC':'Ser', 'AGT':'Ser', 'AGA':'Arg', 'AGG':'Arg',
    'CTA':'Leu', 'CTC':'Leu', 'CTG':'Leu', 'CTT':'Leu',
    'CCA':'Pro', 'CCC':'Pro', 'CCG':'Pro', 'CCT':'Pro',
    'CAC':'His', 'CAT':'His', 'CAA':'Gln', 'CAG':'Gln',
    'CGA':'Arg', 'CGC':'Arg', 'CGG':'Arg', 'CGT':'Arg',
    'GTA':'Val', 'GTC':'Val', 'GTG':'Val', 'GTT':'Val',
    'GCA':'Ala', 'GCC':'Ala', 'GCG':'Ala', 'GCT':'Ala',
    'GAC':'Asp', 'GAT':'Asp', 'GAA':'Glu', 'GAG':'Glu',
    'GGA':'Gly', 'GGC':'Gly', 'GGG':'Gly', 'GGT':'Gly',
    'TCA':'Ser', 'TCC':'Ser', 'TCG':'Ser', 'TCT':'Ser',
    'TTC':'Phe', 'TTT':'Phe', 'TTA':'Leu', 'TTG':'Leu',
    'TAC':'Tyr', 'TAT':'Tyr', 'TAA':'Stop', 'TAG':'Stop',
    'TGC':'Cys', 'TGT':'Cys', 'TGA':'Stop', 'TGG':'Trp'
}

# Define the replicating function
def replicate_dna(dna_sequence):
    """
    Replicate the DNA sequence by creating a complementary strand.
    
    Parameters:
    dna_sequence (str): The DNA sequence to replicate.
    
    Returns:
    str: The replicated DNA sequence.
    """
    replicated_sequence = ''
    for base in dna_sequence:
        replicated_sequence += base_pairs[base]
    return replicated_sequence

# Define the transcribing function
def transcribe_dna(dna_sequence):
    """
    Transcribe the DNA sequence into an RNA sequence.
    
    Parameters:
    dna_sequence (str): The DNA sequence to transcribe.
    
    Returns:
    str: The transcribed RNA sequence.
    """
    rna_sequence = ''
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            rna_sequence += 'U'
        elif nucleotide == 'T':
            rna_sequence += 'A'
        elif nucleotide == 'G':
            rna_sequence += 'C'
        elif nucleotide == 'C':
            rna_sequence += 'G'
    return rna_sequence

# Define the translating function
def translate_rna(rna_sequence):
    """
    Translate the RNA sequence into a protein sequence with three-letter amino acid names.
    
    Parameters:
    rna_sequence (str): The RNA sequence to translate.
    
    Returns:
    str: The translated protein sequence with three-letter amino acid names.
    """
    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if len(codon) < 3:
            break
        dna_codon = codon.replace('U', 'T')
        if dna_codon in DNAcodon_table:
            amino_acid = DNAcodon_table[dna_codon]
            if amino_acid == 'Stop':
                protein_sequence += 'Stop '
                break
            else:
                protein_sequence += amino_acid + ' '
        else:
            protein_sequence += 'X '  # Unknown codon
    return protein_sequence.strip()  # Remove trailing space


# ---------------------------- Main functions ----------------------------
def main():
    # DNA sequence
    dna_sequence = 'GATTAGGTAACTGTGATTCGTACGTAACGTGACGATATTAGCATCCACCGCATACAGACGATATGCATAGCTGATCATATCGCC'

    # Replicate the DNA sequence
    replicated_sequence = replicate_dna(dna_sequence)
    print("Replicated DNA sequence:", replicated_sequence)

    # Transcribe the DNA sequence into an RNA sequence
    rna_sequence = transcribe_dna(dna_sequence)
    print("Transcribed RNA sequence:", rna_sequence)

    # Translate the RNA sequence into a protein sequence
    protein_sequence = translate_rna(rna_sequence)
    print("Translated protein sequence:", protein_sequence)

if __name__ == "__main__":
    main()

