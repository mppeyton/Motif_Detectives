#!/usr/bin/env python3
import sys
import re

#file_gff = sys.argv[1]
file_gff = "/media/cyntsc/bba65e83-4bd6-4574-8f64-10c88f588cf4/CSHL_Motif_Detectives/Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"

gene_feature={}
x = 5
P1 =  3750
P2 =  3800



with open (file_gff,'r') as gtf:
  for line in gtf:
    x+=1
    if x==5: break 
    line = line.rstrip()
    if line.startswith('#'):
      continue
    else:
      I, Wormbase, feature, start, end, a, strand, b, description = line.split('\t')
      line2 = [Wormbase, feature, start, end,description]
      if P1 >= int(start): 
          if P2<= int(end):
            gene_feature.setdefault(I, []).extend([line2]) 

      #gene_feature[I] = Wormbase, feature, start, end, a, strand, b, description
      #gene_feature.setdefault(I, []).extend([line2]) 

# print(gene_feature)  

for key, values in gene_feature.items():
    for i in values:
        print(key, " : ", i)



#for k in gene_feature:
#    print(k[0])
