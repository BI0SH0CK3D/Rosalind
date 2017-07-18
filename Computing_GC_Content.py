from __future__ import division
import re

def gc_content(seq):
	g_count = seq.count("G")
	c_count = seq.count("C")
	gc_perc = float(((g_count + c_count) / len(seq)) * 100)
	return gc_perc

data = open('Rosalind.txt', 'r').read()
clean = data.replace('\n', '')
header = clean.split('>')

d ={}
for item in header:
	x = re.findall('(.*[0-9])(.*)', item)
	for item in x:
		d[item[0]] = item[1]

for item in d:
	d[item] = gc_content(d[item])

highest = ''
count = 0
for item in d:
	if d[item] > count:
		highest = str(item), d[item]

with open('out.txt', 'w') as outfile:
	outfile.write(str(highest[0]))
	outfile.write('\n')
	outfile.write(str(highest[1]))
