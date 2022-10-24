#!/usr/bin/env python3 

# 22Oct2022 
# Written by: Aparna Mariyam Thomas & Mina Peyton
# CSHL Programming for Biolgy - Final Project: Motif Detective
# Input: fasta file
# Output: dictionary {Chromosome_number: sequence}

import glob
import re
 
cgenome = {}
 
for file_name in glob.glob('C*.fa'):
	seq = ''
	with open(file_name,'r') as raw:
#		print(name)
		label_regex = re.compile(r'([IVX]+)')
		label = str(label_regex.findall(file_name)).strip('[]')
		label = label.replace("'","")
#		print(label)
		chromosome_label = 'Chromosome.'+label
#   	print(chromosome_label)
		for line in raw:
			if line.startswith('>'):
#				print(line)
				next
			else:
				line = line.rstrip()
				seq += line
	cgenome[chromosome_label]=seq

print(cgenome)

#for i in cgenome.keys():
#	print(i,cgenome[i][0:3])
