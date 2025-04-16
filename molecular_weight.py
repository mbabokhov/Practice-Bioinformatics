# Takes protein input as string, iterates over string with a loop to return amino acids, sums the molecular weights of the amino acids to get the molecular weight of the protein


# Dictionary containing one letter amino acid code with corresponding mass.
# Mass is average isotopic mass in Daltons (Da) from Expasy findmod: https://web.expasy.org/findmod/findmod_masses.html#AA

amino_acid_mass = {
    'D': 115.1,
    'E': 129.1,
    'H': 137.1,
    'C': 103.1,
    'Y': 163.2,
    'K': 128.2,
    'R': 156.2,
    'A': 71.1,
    'F': 147.2,
    'G': 57.1,
    'I': 113.2,
    'L': 113.2,
    'M': 131.2,
    'N': 114.1,
    'P': 97.1,
    'Q': 128.1,
    'S': 87.1,
    'T': 101.1,
    'V': 99.1,
    'W': 186.2
}

# Prompt user for protein sequence input (removes whitespace, non letters, and capitalizes)
user_sequence = input('Input protein sequence: ').upper().replace(' ', '')
filtered_sequence = ''.join(filter(str.isalpha, user_sequence))

# Prints length of protein sequence
print('Protein length: ' + str(len(filtered_sequence)) + ' residues')

# Calculates protein molecular weight (mass) in Daltons as the sum of amino acid mass
protein_mass = 0
for residues in filtered_sequence:
    protein_mass += (amino_acid_mass[residues])

# Prints the result together with link to Expasy to compare
print('Molecular weight: ' + str(round(protein_mass, 1) + 18.0) + ' Daltons')
print('Compare to Expasy result at: https://web.expasy.org/compute_pi/')
