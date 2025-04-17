# Takes protein input as string, iterates over string with a loop to return amino acids, sums the hydropathy index of the amino acids and divides by the length of the input to get mean hydropathy


# Dictionary containing one letter amino acid code with corresponding hydropathy index.
# Hydropathy valuse are calculated with the PARCH model, using simulated water interactions from: Qin et al. (2025) DOI: 10.1021/acs.jcim.4c02415 Table 3 TIP3P column

hydropathy = {
    'D': 9.1,
    'E': 7.4,
    'H': 7.5,
    'C': 4.0,
    'Y': 8.4,
    'K': 10.0,
    'R': 8.4,
    'A': 4.4,
    'F': 6.0,
    'G': 6.0,
    'I': 4.4,
    'L': 4.5,
    'M': 5.7,
    'N': 5.8,
    'P': 6.6,
    'Q': 6.1,
    'S': 6.6,
    'T': 6.2,
    'V': 4.8,
    'W': 6.9
}

# Prompt user for protein sequence input and filters (removing whitespace, numbers/symbols, and lower case)
user_sequence = input('Input protein sequence: ').upper().replace(' ', '')
filtered_sequence = ''.join(filter(str.isalpha, user_sequence))

# Calculates the sum of protein hydropathy index as the sum of amino acid hydropathies
hydropathy_sum = 0
for residues in filtered_sequence:
    hydropathy_sum += (hydropathy[residues])

# Calculates the mean hydropathy index as the sum divided by number of residues
hydropathy_mean = hydropathy_sum / len(filtered_sequence)

# Print the result
print('The mean hydropathy index is: ' + str(round(hydropathy_mean, 1)))
