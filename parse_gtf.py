#!/usr/bin/env python3
import sys
import re

file_gff = "/Users/student/PFB_Brianda/Files/Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"

gene_feature = {}
with open (file_gff,'r') as gtf:
  for line in gtf:
    line = line.rstrip()
    if line.startswith('#'):
      continue
  else:
    I, Wormbase, feature, start, end, a, strand, b, description = line.split('\t') 
    line2 = [I, Wormbase, feature, start, end, description]
    if P1>= int(start):
      if P2<= int(end):
        gene_feature.setdefault(I,[]).extend([line2])

print(gene_feature)   



 print(line2)






#    for i in I:
#      chrs=i
#    for c in chromosomes:
#      c=chromosomes['chromosome']
#      chrs_list.append(chrs)
#    print(chromosomes)  
#    for e in feature:
#      ftr=feature
#      gene_fauture(feature) += ftr
#      ftr_list.append(ftr)
#    print(gene_feature)
#    print(ftr)
#    for s in start:
#      st= start
#    print(st)
#    for n in end:
#      en= end
#    print(en)
#    chromosomes['chromosome']=chrs
#    gene_feature_d['gene_feature']=ftr
#    coordinates_db['coordinates']=coordinates_ds
#    coordinates_ds['start','end']=st,en
    #descr_list['description']=description
#     genome['chromosome']={I:{{'gene_feature':feature},{'coordinates':{'start':start,'end':end}},{'description':description}}}
#print(gene_feature_d)
    
  # print(description)
#descr_list.append(description)
#print(descr_list)
#  for descr in descr_list:
#    split_descr = descr.split(';')
#def gtf_parse(



  
