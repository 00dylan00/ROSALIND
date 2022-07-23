#!/usr/bin/env python3

import sys

class fasta():
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def read(self):
        f = open(self.input,"r")
        list_seq=[]
        for line in f:
            list_seq.append(line.rstrip("\n"))
        return(list_seq[0],list_seq[1])
    def find_motif(self):
        (seq,motif)=fasta.read(self)
        list_positions=[]
        for i in range(0,len(seq)):
            if seq[i:i+len(motif)] == motif:
                list_positions.append(i+1)
        return list_positions
    def write_result(self):
        list_positions=fasta.find_motif(self)
        f = open(self.output,"w")
        for position in list_positions:
            f.write("%s " %(str(position)))
        f.close

result = fasta(sys.argv[1],sys.argv[2])
result.write_result()