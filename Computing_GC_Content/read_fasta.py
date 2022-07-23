#!/usr/bin/env python3
########################################################
# READ FASTA IN PYTHON
# (1) Define function
# (2) Define function to read file
#	
########################################################
# (1) Imports

import sys
import re


# (2) Define Class
class fasta_seq():
	def __init__(self, file, output):
		self.file = file
		self.output = output


	def read_fasta(self):
		text = open(self.file, "r")
		dictionary = {}
		secuencia = ""
		for line in text:
			if re.match('^>Ros*',line):
				if secuencia != "":
					dictionary[identifier]=secuencia
				identifier = line.strip('\n')[1:]
				secuencia = ""
			else:
				secuencia = secuencia + line.strip('\n')
		dictionary[identifier]=secuencia
		return dictionary
	
	def gc_count(self):
		dictionary_seq = fasta_seq.read_fasta(self)
		dictionary_gc = {}
		for key,values in dictionary_seq.items():
			i_tot = 0
			i_gc = 0
			for letter in values:
				i_tot += 1
				if letter == 'G' or letter == 'C':
					i_gc += 1
			dictionary_gc[key] = i_gc/i_tot
		return (dictionary_gc)

	def highest_gc(self):
		dc_gc = fasta.gc_count()
		id = max(dc_gc, key=dc_gc.get)
		gc_value = max(dc_gc.values())
		f = open(self.output, "w")
		f.write("%s\n%f" %(id, gc_value*100))
		f.close

try:
	fasta = fasta_seq(sys.argv[1], sys.argv[2])
	fasta.highest_gc()
except:
	print("Error!! Example of use:\n ./read_fasta.py input.file output.file")