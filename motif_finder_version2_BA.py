#!/usr/bin/env python3
#R is A or G
#Y is T or C
import sys
import re
import os
import gzip 

#line counter
# length line
#change regular expression
# plus one
# enumerate motifs
#(r”[A/G]G[G/T]T[C/G]A.....[A/G]G[G/T]T[C/G]A“)


#In this following line: open_fasta is a function defined in md_fasta_parser.py and was imported to this script motif_finder_version2_BA.py
#the function motif_finder was created to look for specific motifs in the genome
from md_fasta_parser import*

motif=r"([A|G]G[G|T]T[C|G]A.....[A|G]G[G|T]T[C|G]A)"
fasta_file = sys.argv[1]
genome = open_fasta(fasta_file)
def motif_finder(genome, motif):
  genome2=genome
  with open ('motif_hit_out.txt','w') as output:
      output.write('#chr\tmotif\tstart\tend\n') 
      for chromosome in genome2:
        for i in re.finditer(motif, genome2[chromosome]):
          find1=i.group(0)
          start1=i.start(0) + 1
          end1=i.end(0)
          output.write(f'{chromosome}:\t{find1}\t{start1}\t{end1}\n')
  return


def main():
    progname = sys.argv[0]

    usage = "\n\n\tusage: {} sequence motif\n\n\n".format(progname)
  
    if len(sys.argv) < 1:
      sys.stderr.write(usage)
      sys.exit(1)
#capture comand-line arguments
motif_finder(genome, motif)
print('Confirm Finish')
sys.exit(0)


if __name__ == "__main__":
    main()
    
