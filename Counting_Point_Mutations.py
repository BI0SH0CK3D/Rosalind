string1 = "TGTCGAATCGTCTCGGGGGCTACTATTGGGTGTCGCATGGTGCGTCTGTAGGGTCTTATTGGGGCTAACACATCACTGGCATATCTACCTCTAAGTCAAAGGTTTCCGTTATAAAAGGCTCCTCGCCACCACGATGTGACGATGTCCACCAGGCTGTGCCAGACCCGATCGGTGCCCCTCAATAGGTATCTCACGTAACGGCCCTTTGACACCTTAGTTTTGAAGGCAGGGGCCCTGTATTAGTTGCACGCCGGAAATCAAACCCGCCGTGGTCAGTTCTGGCGGTTACCTGAGGCGACTATCTGTATCCTGCCGGACGCGGGACATTCTTCCATATGAGTGTTCAGGGATTACCTCTGGGCTGGGTCAGTGGCGAGACCCGTCTCCCCTGATACAGTATACGCTCGTCCGGCGTGGCTCGATATTATCGGATGTCAAGCCAATGGAAGGGACTAACAATTGGTAACCGCAAGGCACGGAGAGTCGTGCAATCCACGAGATTTAGCGGGCGCGCGGGTATCGCGATGGGGCAAAGGATGTCTCGCTGCCCCGTTGACGGTTTACCGAATGGATCCGGATCGGGCTGACTTTCTAAGCGGCCAATAGTGGAAATGAGGTGCCGCGACGGAATCTATAGGTTCACCACATTCGATAGCGAAAATTCGAGGCATTTGCGTCGCCCCTTAATTCGACCTCTTTTCTGTGTTAACCGTTCGGTCGCTCCACAGGAAGACGTGATTCTCGCAGGATAGTATAATGACGACTTCAATGGACAGCTCCATGTATCAGACGTAAAACGGACCTAACGAAGCACGGCGTTATCGGCGCACTTGTTAGAAGCTAGTTATTAGTCTCCCCCGCGAATTACAAGTAAGATTGTCTCAGAAATAGCGTCCCGGTTATCCGTTAGTTACTAATAACACGAA"
string2 = "TGTCGGTTATTTCAGAGGGCACGGGTTAGGTATTTCAGAGATCTCGCAAAACTGCTAATTCTGAGTAACACCTTCGCGGGTTATCGATCTAAAATGCCAGTCTTTGCGCTCCTCCAGAAACGACGCTCCCTCGGTTCAGCTCTGATCATCTGGCTCAAGCAAACGACCTCAAGGTCACACATTGGGTCTATCTCTGAAAGGTTTGTAGTGGTCTCGCACTTATACAAATGGAGCAACTTTTGAGAGCACCATGGAGCTACAAGCGGGCGGAGCCCGCATTGTCGGCGGCCGCAGGCTCCTTCCTGGTTCATTCAATACGTAGTCGAGGGTGTCATATCGGCCCATAAGACTCGCGTTAGGTCTGAGACAAGGATCGCTCACGCCGGGAATGCACCCGCACTCGCCGAACTGGCGAGGGTCACTTCTTACAGATTTTTAAATACCGAAAGGGATAGGCAATTTCTAACGTCAGGGCTTCCAAACGTGCGCCATTGCCGCTTGCTATCTGGGCCTGCGCCCGTGCAGGTAGTAAAAGGATGGCGTAGAGCTCAGGTATGGTAGGATCCTATGACTAGGGACGTGGAAGACGTATAAATCAGCAACTTGTGTCTATTCCATGCGGGGCAAGGATCAATACTACCTAACGGTTATCTCACACGCATTTGAATCATCTTATGCGGATCGGGAACAGAACAATGAGTGTTCAAAATCTATCGACTGCTGGTTACGAAGGAGGGCTTGCTACATACTTGACATACTCACACTGCAGAGGCCTGCAGTCTGTATATCACATACTAAGGAACTACCTGAGACCCTCGTCACCCTCAGGGTTAATAGAGGCCTGATGAGGGTCTCCACCGCTAATCTCAATTCTGTTTGTCACCCACACCGTGTCGCTATTCGACAGTGTTTGCTTATAGCTCTTA"

count = 0
for i in range(len(string1)):
	if string1[i] != string2[i]:
		count += 1
	i += 1
print count