#!/usr/bin/env python3

#this is the initial script for the C. elegans  genome gff parser, however, this will be substituted by parse_gft2.py
  
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
chr_list = []
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
    line2 = I,feature,start,end,description
    chr_list.append(line2)
  print(chr_list)      

#      genome['chromosome']=[I:{{'gene_feature':feature},{'coordinates':{'start':start,'end':end}},{'description':description}}]
#print(gene_feature_d)
    

  
