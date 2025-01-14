x = open(r'Path_to_fasta file', 'r')

file_lines = x.readlines()

x.close()

seq_id = []
sequence = str()
sequence_array = []

dict_seq_id_seq = {}

for k in file_lines:
    if ">" in k:
        seq_id.append(k)
for k in file_lines:
    if ">" in k:
        sequence_array.append(sequence)
        sequence = str()
    else:
        sequence = sequence +k

sequence_array.append(sequence)

del sequence_array[0]

for k in range(len(seq_id)):
    seq_id[k] = seq_id[k].replace('\n', "")
    
for k in range(len(sequence_array)):
    sequence_array[k] = sequence_array[k].replace('\n', "")


array_extracted = []
array_extracted2 = []
stop_codons = ["UAG", "UAA", "UGA"]
start_codon = ["AUG"]


for k in range(len(sequence_array)):
    to_be_extracted = sequence_array[k]
    found_start_codon_position = []
    found_stop_codon_positions = []
    extracted = []
        
    n = len(to_be_extracted)
    m = 0
    
    while m < n-2:
    # extract a three-nucleotide subsequence
        possible_codon = to_be_extracted[m:m+3]
        if possible_codon in start_codon:
            found_start_codon_position.append(m)
        if possible_codon in stop_codons:
            found_stop_codon_positions.append(m)
        m = m + 1
    
    array_extracted.append(to_be_extracted[found_start_codon_position[0]:found_stop_codon_positions[0]+3])
    array_extracted2.append(to_be_extracted[found_start_codon_position[0]+3:found_stop_codon_positions[0]]) 
   
    
coding_region = str()

for k in range(len(seq_id)):
    coding_region = coding_region+seq_id[k] + "\n" + array_extracted[k] +"\n"

save_coding_region = open(r'Path_to_this\coding_region.txt', 'w+')
save_coding_region.write(coding_region)
save_coding_region.close()

save_coding_region = open(r'Path_to_this\coding_region.fasta', 'w+')
save_coding_region.write(coding_region)
save_coding_region.close()

coding_region1 = str()

for k in range(len(seq_id)):
    coding_region1 = coding_region1+seq_id[k] + "\n" + array_extracted2[k] +"\n"

save_coding_region = open(r'Path_to_this\coding_region_without_start_stop_codons.txt', 'w+')
save_coding_region.write(coding_region1)
save_coding_region.close()

save_coding_region = open(r'Path_to_this\coding_region_without_start_stop_codons.fasta', 'w+')
save_coding_region.write(coding_region1)
save_coding_region.close()