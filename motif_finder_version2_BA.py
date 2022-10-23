#!/usr/bin/env python3
#R is A or G
#Y is T or C
import sys
import re
import os

#line counter
# length line
#change regular expression
# plus one
# enumerate motifs
#(r”[A/G]G[G/T]T[C/G]A.....[A/G]G[G/T]T[C/G]A“)

from md_fasta_parser import*

#motif=r"([A|G]G[G|T]T[C|G]A.....[A|G]G[G|T]T[C|G]A)"
#dna = {'chromosome1':'AGTTGAGGGGGAGTTCATCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGGAAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTATTACTATATAAAGTACTGCTGCGAGGCTTGCCGTGTTGCATTTTGTTTAGTACAAGACATGTCTGGGCGCGGCAGGGTCATTTTTGGGTCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCAAAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGTGGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTAATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTCAGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGAAGGTCATAGTTAAGGTCAATTTCTTAAGAACACTTAAACGTATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGTGCCCCTTTCAGCATTACTTAGTGGTTAAAA','chromosome2':'AGCACCCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACGTCGCATCTCCACCGTCTCGCGGATCGACCCAGCGAAGTCAGGTTCATTTTTGGTTCACCTCCCGCCCCCAAAGTCCCCCAAATCTTGCAGTTCCCTCCTAAATCCTCCCCATATAAACCAACCCCCCGCCCTCAGATCCCTAATCCCATCGCAAGCATCAGACTCCCTCCAAAGCAGGCAGCAGCTCCTCTTCTTCCTAATCACACTATCTCGGAGAGGAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCAGGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCTTCGGAGGCTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTGATCTGTGCTGTCGTAGATGAGATTTACTGATTTGGCGTGCGCCGGTTGTATTCTGTCATGGGGTTCAGTGGGCTGTGTAATACCTTGCTCTGTACTTCTGTTCAATGCAATCACTTCTATTCTGAA'}
def motif_finder(sequence, motif):
  with open ('motif_hit_out.txt','w') as output:
    output.write('#chr\tmotif\tstart\tend\n')
    for chromosome in sequence:
      for i in re.finditer(motif,sequence[chromosome]):
        find1=i.group(0)
        start1=i.start(0) + 1
        end1=i.end(0)
        output.write(f'{chromosome}:\t{find1}\t{start1}\t{end1}\n')
  return output


def main():
    progname = sys.argv[0]
#    fasta_file = sys.argv[1]
#    motif = sys.argv[2]

    usage = "\n\n\tusage: {} sequence motif\n\n\n".format(progname)
  
    if len(sys.argv) < 2:
      sys.stderr.write(usage)
      sys.exit(1)
#capture comand-line arguments
    fasta_file = sys.argv[1]
    motif = sys.argv[2]
    genome = open_fasta(fasta_file)
    motif_match = motif_finder(genome, motif)
    print(motif_match)

#    sys.exit(0)


if __name__ == "__main__":
    main()
    
