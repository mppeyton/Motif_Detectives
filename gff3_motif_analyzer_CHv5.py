#!/usr/bin/env python3

import sys
import gzip

# parse hits from motif_finder.py

hit_dict = {}
motif_dict = {}

with open('motif_hit_out.txt','r') as hits:
	for line in hits:
		line = line.rstrip()
		if line.startswith('#'):
			continue
		chromosome, motif, p_start, p_end = line.split()
		motif_dict[motif] = [p_start, p_end]
		if chromosome not in hit_dict:
			chromosome = 'c' + chromosome.lstrip("C").rstrip(":")
			hit_dict[chromosome] = motif_dict

# parse .gff3 file

gene_feature={}

for key in hit_dict:
	file_gff = 'Caenorhabditis_elegans.WBcel235.108.%s.gff3.gz' % key
	with gzip.open(file_gff,'rt') as gtf:
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
				continue
			line2 = 'Chr' + Chromosome + '\t' + feature + '\t ' + start + '\t' + end + '\t' + new_description
#	loop over hits in motif_dict and feed in start and end coordinates
			for hit in motif_dict:
				p_start = motif_dict[hit][0]
				p_end = motif_dict[hit][1]
				line1 = motif + '\t' + p_start + '\t' + p_end
# find motif positions of hits in the annotated genome
				if int(p_start) >= int(start) and int(p_end) <= int(end):
# extend data to gene_feature dict
					gene_feature.setdefault('Chromosome.' + Chromosome, []).extend([line1 + '\t' + line2])

# create output file
with open('mapped_motif_hits.out', 'w') as output:
	output.write(f"# motif\tstart\tend\tchr\tfeature\tstart\tend\tID/description\n")
	for chromosome, entries in gene_feature.items():
		for mapped_hit in entries:
			output.write(mapped_hit + '\n')
print("written file mapped_motif_hits.out")
