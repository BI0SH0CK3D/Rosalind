import re

string = open('rosalind_subs.txt', 'r').read()
string = string.replace('\n', '')
# string = "GATATATGCATATACTT"

motif = 'ATAT'

position = 0
increment = 4

motif_locales = []

while position + increment != (len(string)):
	target = string[position:position+increment]
	if motif == target:
		motif_locales.append(position + 1)
		pass
	position += 1

with open('Finding a Motif in DNA2.txt', 'w') as output:
	for item in motif_locales:
		output.write(str(item) + ' ')
output.close()