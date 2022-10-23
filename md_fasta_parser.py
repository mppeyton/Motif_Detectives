#!/usr/bin/env python3

import glob
import re
import sys
cgenome = {}

def open_fasta(fasta_file):
  for file_name in glob.glob(fasta_file):
    seqs = []
    with open(fasta_file,'r') as raw:
      #print(name)
      label_regex = re.compile(r'([IVX]+)')
      label = str(label_regex.findall(file_name)).strip('[]')		
      label = label.replace("'","")
	#	print(label)
      chromosome_label = 'Chromosome.'+label
#		print(chromosome_label)
      for line in raw:	
        if line.startswith('>'):
	#			print(line)
          next
        else:
          line = line.rstrip()
          seqs.append(line)
      sequence = ''.join(seqs)
      cgenome[chromosome_label]=sequence
  return cgenome

def main():
  progname=sys.argv[0]
  usage = "\n\n\tusage: {} fasta_file\n\n\n".format(progname)

  if len(sys.argv) < 1 :
    sys.stderr.write(usage)
    sys.exit(1)

#capture command-line arguments 
  fasta_file=sys.argv[1]
  parsed_genome=open_fasta(fasta_file)
  print(parsed_genome)
  sys.exit(0)

<<<<<<< HEAD
=======
if __name__ == "__main__":
    main()
>>>>>>> 4845cfa95510cd7cd6c47d0430ec3c38a876ba70

