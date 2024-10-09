def replicate_dna(dna_sequence):
    replicated_sequence = ''
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            replicated_sequence += 'T'
        elif nucleotide == 'T':
            replicated_sequence += 'A'
        elif nucleotide == 'G':
            replicated_sequence += 'C'
        elif nucleotide == 'C':
            replicated_sequence += 'G'
    return replicated_sequence

def transcribe_dna(dna_sequence):
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

def translate_rna(rna_sequence):
    genetic_code = {
        'AUA': 'Ile', 'AUC': 'Ile', 'AUU': 'Ile', 'AUG': 'fMet',
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
        'UAC': 'Tyr', 'UAU': 'Tyr', 'UAA': '*', 'UAG': '*',
        'UGC': 'Cys', 'UGU': 'Cys', 'UGA': '*', 'UGG': 'Trp'
    }
    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = genetic_code.get(codon, 'X')
        protein_sequence += amino_acid + '-'
    return protein_sequence.strip('-')

dna_sequence = 'GUAUGUCUGCUAUACGUAUCGACUAGUAUAGCGG'
replicated_sequence = replicate_dna(dna_sequence)
rna_sequence = transcribe_dna(replicated_sequence)
protein_sequence = translate_rna(rna_sequence)

print('Replicated DNA sequence:', replicated_sequence)
print('Transcribed RNA sequence:', rna_sequence)
print('Translated protein sequence:', protein_sequence)