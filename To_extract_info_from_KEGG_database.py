#to import all the necessary pacakage for KEGG Database
from Bio import SeqIO
from Bio.KEGG.REST import *
from Bio.KEGG import REST
from Bio.KEGG.KGML import KGML_parser
import os
import random

out_dir = r"Path_to_folder"

# To extract protein in fasta format
result = REST.kegg_get("nve:116616792+nve:5513834 ", "aaseq").read()
print(result)

os.chdir(out_dir)
#to extract specific gene from all the species
result = REST.kegg_find("nve","pyruvate decarboxylase").read()
f = open("Lysine_biosynthesis_nemato.txt", "x")
f.write(result)

# to extract single protein
result = REST.kegg_get("hmg:100199027", "aaseq").read()
print(result)

# to get the all the pathways name with accession number
result = REST.kegg_list('pathway', 'hmg').read()
print(result)

#print information about the pathway database
result = REST.kegg_info("pathway").read()
 print(result)

#to get the all the gene names invloved in a single pathway
result = REST.kegg_find("genes", "hmg00240").read()
print(result)

#to get the list of all the genes for organism
result = REST.kegg_list("hmg").read()
print(result)
#to get the info about species
result = REST.kegg_info("hmg").read() 
print(result)

#to get the cpd info of protein
result = REST.kegg_get("cpd:C00051").read()
print(result)

# to get the complete specific pathway image 
pathway = KGML_parser.read(kegg_get("hmg00240", "kgml"))
print(pathway)

#to get the image of pathway map
Image(kegg_get("map01100", "image").read())
 result = REST.kegg_get("hmg00240", "image").read()
 Image(result)

# view the contents of ko_map KGML
ko_map = REST.kegg_get("ko00061", "kgml").read()
head(ko_map, 20)
