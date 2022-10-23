#!/usr/bin/env python3

import sys

# parse hits from motif_finder.py

hit_dict = {}

with open('motif_hit_out.txt','r') as hits:
	for line in hits:
		line = line.rstrip()
		if line.startswith('#'):
			continue
		chromosome, motif, p_start, p_end = line.split()
		hit = chromosome + ": " + motif
		hit_dict[hit] = [p_start, p_end]

# parse .gff3 file

file_gff = "Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"
gene_feature={}

with open (file_gff,'r') as gtf:
# skip over the first 9 lines of the file
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
		line2 = 'Chr' + Chromosome + '\t' + feature + '\t ' + start + '\t' + end + '\t' + new_description
#	loop over hits in hit_dict and feed in start and end coordinates of motifs
		for hit in hit_dict:
			p_start = hit_dict[hit][0]
			p_end = hit_dict[hit][1]
			line1 = motif + '\t' + p_start + '\t' + p_end
			print(p_start + " : " + p_end)
# find motif positions of hits in the annotated genome
			if int(p_start) >= int(start) and int(p_end) <= int(end):
# extend data to gene_feature dict
				gene_feature.setdefault('Chromosome.' + Chromosome, []).extend([line1 + '\t' + line2])
#	print(gene_feature)
# create output file
with open('motif_hits_mapped.out', 'w') as output:
	output.write(f"# motif\tstart\tend\tchr\tfeature\tstart\tend\tID/description\n")
	for chromosome, entries in gene_feature.items():
		for mapped_hit in entries:
			output.write(mapped_hit + '\n')

		
