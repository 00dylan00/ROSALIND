#!/usr/bin/env python3
import sys
import rna_prot

class fasta():
    def __init__(self,input,output):
        self.input = input
        self.output = output
    def read_file(self):
        f=open(self.input,"r")
        sequence=""
        for line in f:
            sequence = line.rstrip("\n")
        return(sequence)
    def translate(self):
        sequence = fasta.read_file(self)
        dict = rna_prot.dict_rna_prot
        prot_seq = ""
        for i in range(0, len(sequence)-2,3):
            if dict[sequence[i:i+3]] != "Stop":
                prot_seq = prot_seq + dict[sequence[i:i+3]]
        return(prot_seq)
    def write_file(self):
        f = open(self.output, "w")
        f.write(fasta.translate(self))
        f.close

try:
    result = fasta(sys.argv[1], sys.argv[2])
    result.write_file()
except:
    print("Error!!!Try\n./script.py input.file outpu.file")