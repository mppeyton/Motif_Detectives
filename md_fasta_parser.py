#!/usr/bin/env python3

import glob
import re

cgenome = {}

for file_name in glob.glob('C*.fa'):
	seqs = []
	with open(file_name,'r') as raw:
	#	print(name)
		label_regex = re.compile(r'([IVX]+)')
		label = str(label_regex.findall(file_name)).strip('[]')		
		label = label.replace("'","")
	#	print(label)
		chromosome_label = 'Chromosome.'+label
#		print(chromosome_label)
		for line in raw:	
			if line.startswith('>'):
	#			print(line)
				next
			else:
				line = line.rstrip()
				seqs.append(line)
		sequence = ''.join(seqs)
		cgenome[chromosome_label]=sequence

print(cgenome)
#for i in cgenome.keys():
#	print(i,cgenome[i][0:3])


