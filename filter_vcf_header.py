#Daniel Ence 
#April 13, 2017

import sys
import os
import re

#open a vcf file

curr_file = "Ptaeda.V1_1.wegrzyn_transcriptom.freebayes.vcf"
#curr_file = "tmp2"
vcf_file = open(curr_file, 'r')
#make a list of the contigs with variants
variants_contig_hash = {}	
for line in vcf_file:
	header_pattern = re.compile("^#")
	if(not header_pattern.search(line)):
		parts = line.split("\t")
		variants_contig_hash.setdefault(parts[0],1)
			
vcf_file.close()

#output a new vcf_file with only the contigs with variants in the header
vcf_file = open(curr_file,'r')
contig_header_pattern=re.compile("^##contig")
for line in vcf_file:
	line = line.strip()
	if(contig_header_pattern.search(line)):
		header_line_parts=re.split("[=,]",line)
		contig_ID=header_line_parts[2]
		#print "contig ID is:\t" + contig_ID
		#print variants_contig_hash
		if(variants_contig_hash.has_key(contig_ID)):
			print line
	else:
		print line
vcf_file.close()		
