#!/usr/bin/env python3
import sys
import re

file_gff = "/media/cyntsc/bba65e83-4bd6-4574-8f64-10c88f588cf4/CSHL_Motif_Detectives/Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"

# This is the dict where I will save the matched positions
gene_feature={}

# These are simulated data (static positions)
P1 =  3750
P2 =  3800

with open (file_gff,'r') as gtf:
  for line in gtf:
    line = line.rstrip()
    if line.startswith('#'):
      continue
    else:
      I, Wormbase, feature, start, end, a, strand, b, description = line.split('\t')
      line2 = [Wormbase, feature, start, end, description]
      # I compare each line to evaluate the positions, if match, then I add it to the gene_feature dict
      if P1 >= int(start): 
          if P2<= int(end):
            # With extend I add the data to be retrieved in the same dict
            gene_feature.setdefault(I, []).extend([line2]) 

      #gene_feature.setdefault(I, []).extend([line2]) 

# print(gene_feature)  

# Here I see the results 
for key, values in gene_feature.items():
    for i in values:
        print(key, " : ", i)



