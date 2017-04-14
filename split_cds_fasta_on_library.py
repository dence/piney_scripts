#Daniel Ence 
#April 14, 2017

import argparse
import os
import re
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def main(fasta_file,separator):
	#open the fasta file
	#read through the fasta file
	#grab the header line
	#keep the header line and the sequence line(s)
	#split the header to get the library names.
	#output (append) to "fasta_file" sub library
	curr_handle = SeqIO.parse(fasta_file,"fasta")
	for seq in curr_handle:
		curr_id = seq.id
		curr_id_parts = re.split(separator,curr_id)
		curr_lib = curr_id_parts[0]
		curr_lib_fasta = curr_lib + "_" + fasta_file
		curr_lib_fasta_handle = open(curr_lib_fasta,"a")
		curr_lib_fasta_handle.write(">" + curr_id + "\n" + str(seq.seq) + "\n")
		curr_lib_fasta_handle.close()			

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="splits a fasta file on a library ID found in the fasta header of each entry in the fasta header")
	parser.add_argument("--fasta",type=str,help="the file that we're splitting")
	parser.add_argument("--sep",type=str,help="the separator that we're going to split on")
	args = parser.parse_args()
	main(args.fasta,args.sep)

