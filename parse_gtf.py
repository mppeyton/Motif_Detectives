#!/usr/bin/env python3
import sys
import re

#file_gff = sys.argv[1]
file_gff = "/Users/student/PFB_Brianda/Files/Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3"

genome = {}
chromosomes = {}
gene_feature_d = {}
coordinates_db = {}
coordinates_ds = {}
descr_list = []
chrs_list = []
ftr_list = []
st = []
en = []
gene_feature={}

with open (file_gff,'r') as gtf:
  for line in gtf:
    line = line.rstrip()
    if line.startswith('#'):
      continue
    I, Wormbase, feature, start, end, a, strand, b, description = line.split('\t')
    print(line)
#    for i in I:
#      chrs=i
#    for c in chromosomes:
#      c=chromosomes['chromosome']
#      chrs_list.append(chrs)
    print(chromosomes)  
    for e in feature:
      ftr=feature
      gene_feature(feature) += ftr
#      ftr_list.append(ftr)
    print(gene_feature)
#    print(ftr)
    for s in start:
      st= start
#    print(st)
    for n in end:
      en= end
#    print(en)
#    chromosomes['chromosome']=chrs
#    gene_feature_d['gene_feature']=ftr
#    coordinates_db['coordinates']=coordinates_ds
#    coordinates_ds['start','end']=st,en
    #descr_list['description']=description
#     genome['chromosome']={I:{{'gene_feature':feature},{'coordinates':{'start':start,'end':end}},{'description':description}}}
#print(gene_feature_d)
    
  # print(description)
descr_list.append(description)
#print(descr_list)
#  for descr in descr_list:
#    split_descr = descr.split(';')
#def gtf_parse(

  
