dna = 'GCGAGCCGCCCTGAACAACGCCTTGAATCATAGATTTTGTGCTTTTACTGGCTGTTGATAGCATAAGCGCCATATTGATACCGGCAGAATTGTCTTGCTCCCATGTCCTAGATCCACCGTCGTTTACGGTCTGTGTTATTCCCTTACAGCAAAAGCTACAGTAATCTTCCATGAGAGGGTTCACTTTCGTCACTGAACCGCCCCAACAGTTTAGTAATCGTTAGGTCTGCGATACTGAGCACTTAAAATGCTACTGGAGGACCGACGTTGGGCAGACAAACCTATCAACGGTCGGATGAAAGTTCCATACGAACCTGTCTCACGAGCCGTAAGGGGCTACTTCTCTTCTGGGCTGGTGAAGCCCGCCTGGGTCACCAATAGCACTCGGTGGGGACACACACGTCCCGCGAATTAAGTCGGGCTACACACTAGCGATTTTCACAGTTCCGACGGGCGTCGCACCTCGTACCACGAGCAGCTTAATACAATATCTATGACATGCTATGATGTTAGGCTGGGACCAGTTCAGCAGCGGGAGGTCTTTGTAGACTCGTAACTATCTATCGTCCTCGTGGTATCACTCAAGCCTTATCGCAGACCAAAACTTACGGCATTCTGCGATCGCACTGTACTCAATAAACCCTACGCGAGCAGAAAATTGGTTCTGTTTCAATTGTGCTGGGATTCGGATTATATCCAGAGTCCGTGAGAATAGCACCATAGTAAGCGTCGCGTACGTGACGTCTCCTTAATGAGCGAATTGATAATAGGCGTCCCTAGAAAGACTGATACACTTCCAGTCCGAGGGATTACGCCCCCTTCAAGAGAGAGTTCGGCGGAGAATCGGGTAAATCAATAGCCACTCTTGAGGCAGATTGCGGGGGTTGGCTTCTTACTCA'

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

rev_dna = ''.join(reversed(dna))

comp_dna = ''

for item in rev_dna:
    comp_dna += complement.get(item)

with open('Complementing a Strand of DNA (ANSWER).txt', 'w') as out:
    out.write(comp_dna)