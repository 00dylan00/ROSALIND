#!/usr/bin/env python3

import sys
import sequence_data

class fasta():
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def read_file(self):
        f = open(self.input,"r")
        for line in f:
            sequence = line.rstrip("\n")
        return (sequence)
    def calculate_mw(self):
        sequence = fasta.read_file(self)
        dict_mw = sequence_data.dict_mw
        tot_mw = 0
        for letter in sequence:
            tot_mw = tot_mw + dict_mw[letter]
            print (tot_mw)
        return tot_mw
    def calculate_mw_2(self):
        sequence = fasta.read_file(self)
        dict_mw = sequence_data.dict_mw
        list_mw = []
        for letter in sequence:
            list_mw.append(dict_mw[letter])
        return (round(sum(list_mw),3))
    def write_file(self):
        f = open(self.output,"w")
        f.write(str(fasta.calculate_mw_2(self)))

result = fasta(sys.argv[1], sys.argv[2])
result.write_file()