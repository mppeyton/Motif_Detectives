# TEAM Motif_Detectives
Motif detectives proyect for CSHL "Programming for Biology" course 2022

## AUTHORS

Brianda Lopez Aviña / Marleny García Lozano / Bana Abolibdeh / Chrissi Heil / Mina Peyton / Aparna Thomas

Collaboration TA Cynthia Cardinault (Centro de Investiogacion Cientifica de Yucatán)

## Description
The purpose of this project is to offer the user a program to identify an specific motif/consensus sequence, a.k.a transcription factor binding site, on their organism genome of interest. 

The transcription factors (TF) are proteins that activate or repress gene expression by binding to consensus sequences located at the start of the gene (promoter). Determining the localization of TF-binding sequences will help us to identify direct targets gene on genomes; one of the most challenging problems in molecular biology and bioinformatics. 

## Files used 

INPUTS: GENOME.fa, GENOME.gff , selected MOTIF
OUTPUT: FILE.txt 

To test the code developed, we will use the [C. elegans genome](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwicv-qEpPf6AhVTk4kEHQfPAX0QFnoECBQQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCaenorhabditis_elegans&usg=AOvVaw0_aL9Y_xW2S39CMMZfjS5c) (specifically, Chr 1) and the [Retinoic Acid Response Element](https://www.researchgate.net/figure/Alignments-of-known-DR5-RARE-motifs-in-the-promoters-of-the-Cyp26A1-RAR2-RAR2-RAR2_fig1_232304935) motif (RARE-DR5)

**INPUT FILES:**

*FASTA FILE* [Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fftp.ensembl.org%2Fpub%2Frelease-108%2Ffasta%2Fcaenorhabditis_elegans%2Fdna%2FCaenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz&amp;data=05%7C01%7Cbrianda.lavina%40uky.edu%7C2e3e746bc07c4ff37e6208dab3d1e55b%7C2b30530b69b64457b818481cb53d42ae%7C0%7C0%7C638020012360908962%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=8B6wS2qgy9x63e%2FgpBYHPQLxKGsh49EiRrJjqm6VXt4%3D&amp;reserved=0)<br>
*GFF FILE* [Caenorhabditis_elegans.WBcel235.108.chromosome.I.gff3.gz](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fftp.ensembl.org%2Fpub%2Frelease-108%2Fgff3%2Fcaenorhabditis_elegans%2FCaenorhabditis_elegans.WBcel235.108.chromosome.I.gff3.gz&amp;data=05%7C01%7Cbrianda.lavina%40uky.edu%7C2e3e746bc07c4ff37e6208dab3d1e55b%7C2b30530b69b64457b818481cb53d42ae%7C0%7C0%7C638020012360908962%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&amp;sdata=IjQ8oMkJUT6dmwoNK1aUt2NxxDGhMTtEjOVkxfc7Va0%3D&amp;reserved=0)<br>
*MOTIF regular expression - RARE/DR5* ([A|G]G[G|T]T[C|G]A.....[A|G]G[G|T]T[C|G]A)

## Steps

Figure1. Motif finder pipeline
![MOTIF FINDER PROGRAM](https://github.com/Bla880/Motif_Detectives/blob/main/Fig1.MotifPipeline.png)

**1. Fasta parser**; extracting data fields from GENOME.fa file ->  included in [motif_finder_version2_BA.py](https://github.com/cyntsc/Motif_Detectives/blob/main/motif_finder_version2_BA.py)<br>
**2. Search for the motif sequence on the genome fasta sequence**; extract *motif coordinates* (# start nucleotide, # end nucleotide) -> [motif_finder_version2_BA.py](https://github.com/cyntsc/Motif_Detectives/blob/main/motif_finder_version2_BA.py)<br>
**3. gff parse**; extract chromosome number, feature (exon, CDS, mRNA, etc), *feature coordinates* (# start nucleotide, # end nucleotide) and description (gene_ID, protein_ID) -> step included on [gff3_motif_analyzer_CHv3.py](https://github.com/cyntsc/Motif_Detectives/blob/main/gff3_motif_analyzer_CHv3.py)<br>
**4. Determine which genes on the genome have the motif** pair *motif coordinates* extracted in Step2 with *feature coordinates* extracted on Step3 to determine where in the chromosome the motif is located. This returns a a list of motifs associated with the gene_ID -> step iincluded on [gff3_motif_analyzer_CHv3.py](https://github.com/cyntsc/Motif_Detectives/blob/main/gff3_motif_analyzer_CHv3.py) <br>
<br>
**Additional step: Application of our scripts on DEGs from RNAseq data** <br>
*Is your motif present in differentally expressed genes?*
To answer that question, we proposed to use RNAseq data from two stages in development of C. elegans: oocyta and one-cell stage embryo. This analysis work running only one code -> SCRIPT NAME: [Op_genes_motifs.py](https://github.com/cyntsc/Motif_Detectives/blob/main/op_genes_motifs.py)<br>

INPUTS: <br>
list of DEGs from data base (already prepared by the authors [up_genes_1cell_embryo.txt](https://github.com/cyntsc/Motif_Detectives/blob/main/up_genes_1cell_embryo.txt)) <br>
list of motif hits obtained in step4 [motif_hits_mapped.out](https://github.com/cyntsc/Motif_Detectives/blob/main/motif_hits_mapped.out) <br>
OUTPUTS: <br>
list of DEGs that have the motif in their sequence (Upregulated_gene_list.txt)

