# -------------- DNA Replication, Transcription, and Translation --------------

# -------------- Given information --------------
template_strand = 'GATTAGGTAACTGTGATTCGTACGTAACGTGACGATATTAGCATCCACCGCATACAGACGATATGCATAGCTGATCATATCGCC'

primer = 'AUCCAUU'


# -------------- Known course definitions --------------

# Define the Pribnow box and -35 region
pribnow_box = 'ATATTA'
minus_35_region = 'AACTGT'

# Define the start codon
start_codon = 'AUG'

# Find the Pribnow box, -35 region, and start codon in the DNA strand
def find_pribnow(dna_strand):
    return dna_strand.find(pribnow_box)

def find_minus_35(dna_strand):
    return dna_strand.find(minus_35_region)

def find_start_codon(dna_strand, pribnow_index):
    return dna_strand.find(start_codon, pribnow_index + 10)

pribnow_index = find_pribnow(template_strand)
minus_35_index = find_minus_35(template_strand)
start_codon_index = find_start_codon(template_strand, pribnow_index)

print('Pribnow Box Index:', pribnow_index)
print('-35 Region Index:', minus_35_index)
print('Start Codon Index:', start_codon_index)

# ----------- Code definitions --------------

# Define the start codon
start_codon = 'AUG'

# Find the start codon in the DNA strand
start_codon_index = template_strand.find(start_codon)


# ----------- Replication ----------------

def replicate_dna(template_strand, primer):
    # Define complementary base pairs
    base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Find complementary strand
    complementary_strand = ''.join(base_pairs[base] for base in template_strand)
    
    return complementary_strand

replicated_strand = replicate_dna(template_strand, primer)
print('Replicated Strand:', replicated_strand)


# ----------- Transcription ----------------

def transcribe_dna(dna_strand):
    # Define RNA base pairs
    rna_base_pairs = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Transcribe DNA into mRNA
    mrna_strand = ''.join(rna_base_pairs[base] for base in dna_strand)
    
    return mrna_strand

mrna_strand = transcribe_dna(replicated_strand)
print('mRNA Strand:', mrna_strand)

# If the start codon is not found, try to find it in the mRNA strand
if start_codon_index == -1:
    start_codon_index = mrna_strand.find('AUG')


# ----------- Translation ----------------

def translate_mrna(mrna_strand, start_codon_index):
    # Define codon table
    codon_table = {
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
    
    # Translate mRNA into amino acids
    amino_acids = ''
    for i in range(start_codon_index, len(mrna_strand), 3):
        codon = mrna_strand[i:i+3]
        amino_acids += codon_table.get(codon, 'X') + ' '
    
    return amino_acids

amino_acids = translate_mrna(mrna_strand, start_codon_index)
print('Amino Acids:', amino_acids)

# Translate the mRNA strand into amino acids
amino_acids = ''
for i in range(start_codon_index, len(mrna_strand), 3):
    codon = mrna_strand[i:i+3]
    amino_acids += codon_table.get(codon, 'X') + ' '