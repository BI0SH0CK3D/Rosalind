dna = "GTTCATGGCCAGCTGTGCACTCGTTGTCACACTTATTGGTCGGCATCGAGTCCCAGTTTAGTGGAGGGGTATCACATTATAGTGCTTGGATAGGTCTATAGGCTAATCTCTTGATATCGTATAACCGCAACCGGTTTGACGTAGGGAGCCGCATAGGGGGATATGGCGCAGCCCTGGTTTCGGCTGTCGCCGTTTAAGAAAGGAACTATATCCTTGAGAATGTACCATGCGTGACGTACGTTACGAATTGCTGGGAGAGCGTTATTGTCTCAGCTACATCATAGTTGAGTAGGATGGGCGGTGGATACAGAGCCCCGGAGCCCGCCCATAACCCGAATTCAGACGTATAAGAGTCTATCCGCACCAGTCTACAACAGCGGACGTAGGCGTCGGCCCAAATGACAAATGATGGTGTAACAGTATCCTTTAAAGCAGGTATCGCTGCCGCCTAACCTTGCCCGAGTGCGTTAACTTACCCTAGATGGTTGTGTACCCACGAGTAAGCTCAATGTTAACACGTCCGCTCAGGAATGGTGCCGAGGGGGGGATCGCTCGGATTCTACAAGCTCGTGTTCATTAGATCGACCACGCAAGCGGTTTCGATCTTTATCACGCCAGATATTTCAGGATCGAGAAAAGTTACCCCTATAACGGAGTCTTCAACTAGATCCAGTCGGATGTAACAGTATCCGTATAATCAGTCCTCCTAACAGAGACCGTCTGAACGAACACGCCTGGCTTGGGGCTGAAATCATAACACTCTTGCTAGAGACAAAGTTATATCGAACAGACAGACACATGCTCAGCGCGCTATATTTGTCCTATTAGTATTTCCTTATAAAAGGTATACAGAAACAGCGCGACTTGAAAGCGGTCTGATTCGGCGTACTGCCAACACGGGGGTATTCAACGCTCAAACTTTTCGTGCAA"

rna = dna.replace("T", "U")

print rna 

with open("output.txt", 'w') as outfile:
	outfile.write(rna)