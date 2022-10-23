#!/usr/bin/env python3

import sys

file_gff = "Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"

#This is the dict where I will save the matched positions
gene_feature={}


with open('Chromosome.1_hits.txt','r') as hits, open (file_gff,'r') as gtf:
	for line in hits:
		line = line.rstrip()
		chromosome,motif,p_start,p_end = line.split()
			for line in gtf:
				line = line.rstrip()	
				if line.startswith('#'):
					continue
				else:
					Chromosome, Wormbase, feature, start, end, a, strand, b, description = line.split('\t')
					line2 = [Chromosome,feature, start, end, description]
			# I compare each line to evaluate the positions, if match, then I add it to the gene_feature dict 
					if int(p_start) >= int(start):
						if int(p_end) <= int(end):
			# With extend I add the data to be retrieved in the same dict
							gene_feature.setdefault('Chromosome.'+Chromosome, []).extend([line2])
					for key, values in gene_feature.items():
						for i in values:
							print(i) 

		
