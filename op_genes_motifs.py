#!/usr/bin/env python3
with open ('/Users/student/Downloads/up_genes_1cell_embryo.txt','r') as genes:
  next(genes)
  for line in genes:
    line = line.rstrip()
    gene , gene_id , fc , pval = line.split('\t')
    line2 = gene_id

    with open('motif_hits_mapped.out','r') as motif_matches:
      next(motif_matches)
      for line3 in motif_matches:
        line3 = line3.rstrip()
        motif, start , end , chromosome , feature , start , end ,description  = line3.split('\t')
        line4 = description
        motif1=motif
        if line2 in line4:
          print('upregulated gene: '+line2+' contains this motif:' +motif1,'annotation',line4)

