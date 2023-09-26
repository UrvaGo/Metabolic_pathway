# this is modified script!!!
import urllib.request
import re
import sys
pathway = 'hsa00010' # glycolysis
url = "http://rest.kegg.jp/get/" + pathway
with urllib.request.urlopen(url) as f:
     lines = f.read().decode('utf-8').splitlines()
     want = 0
     for line in lines:
         fields = line.split()
         ## The list of genes starts here
         if fields[0] == 'GENE':
             want = 1
             ## The line with GENE is different
             print(fields[2].rstrip(';'))
         ## We reached the next section of the file
         elif want == 1 and re.match('^\S', line):
             sys.exit();
         ## We're still in the list of genes
         if want == 1 and len(fields)>1:
             print(fields[1].rstrip(';'))

