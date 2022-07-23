#!/usr/bin/env python3
import sys
from unittest import result
class fasta():
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def count_mutations(self):
        f = open(self.input, "r")
        dictionary = {}
        i = 0
        mutations = 0
        for line in f:
            i += 1
            dictionary[i] = line
        for x in range(0,len(dictionary[1])):
            if dictionary[1][x] != dictionary[2][x]:
                mutations += 1
        return mutations
    def output_mutations(self):
        f = open(self.output, "w")
        f.write(str(fasta.count_mutations(self)))
try:
    result = fasta(sys.argv[1], sys.argv[2])
    result.output_mutations()
except:
    print("Error!! Try:\n ./script.py input.file output.file")