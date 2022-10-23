#!/usr/bin/env python3

import sys

file_gff = "Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"

# This is the dict where I will save the matched positions
gene_feature={}
# Create a dict to save hits with their start and end coordinates
hit_dict = {}

# hit parser
with open('Chromosome.1_hits.txt','r') as hits:
	for line in hits:
		line = line.rstrip()
		chromosome, motif, p_start, p_end = line.split()
		hit = chromosome + ": " + motif
		hit_dict[hit] = [p_start, p_end]
#print(hit_dict)

# Let's check if I can access p_start (list index 0) and p_end (list index 1)
#for hit in hit_dict:
#	print(f"p_start: {hit_dict[hit][0]}, p_end: {hit_dict[hit][1]}")
	
# gff parser
with open (file_gff,'r') as gtf:
# skip over the first 9 lines
	for line in range(8):
		next(gtf)
	for line in gtf:
		line = line.rstrip()	
		if line.startswith('#'):
			continue
		else:
			Chromosome, Wormbase, feature, start, end, a, strand, b, description = line.split('\t')
			split_description = description.split(';')
			if feature == 'gene':
				new_description = split_description[0] + ' ' + split_description[3]
			else:
				new_description = split_description[0] 
# changed line2 into string instead of list
#		line2 = [Chromosome, feature, start, end, new_description]
		line2 = 'Chr' + Chromosome + '\t' + feature + '\t ' + start + '\t' + end + '\t' + new_description
#		print(line2)
#	loop over hits and feed in start and end coordinates from hit_dict
		for hit in hit_dict:
			p_start = hit_dict[hit][0]
			p_end = hit_dict[hit][1]
			line1 = motif + '\t' + p_start + '\t' + p_end
# I compare each line to evaluate the positions, if match, then I add it to the gene_feature dict 
			if int(p_start) >= int(start) and int(p_end) <= int(end):
#			if int(p_start) >= int(start):
#				if int(p_end) <= int(end):
# With extend I add the data to be retrieved in the same dict
# added motif and coordinates to output
#					gene_feature.setdefault('Chromosome.' + Chromosome, []).extend([line2])
					gene_feature.setdefault('Chromosome.' + Chromosome, []).extend([line1 + '\t' + line2])
#print(gene_feature)

with open('motif_hits_mapped.out', 'w') as output:
	output.write(f"# motif\tstart\tend\tchr\tfeature\tstart\tend\tID/description\n")
	for key, values in gene_feature.items():
	#	print(values)
		for i in values:
			output.write(i + '\n')
#			print(i) 

		
