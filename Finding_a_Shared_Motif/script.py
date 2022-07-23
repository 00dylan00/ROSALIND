#!/usr/bin/env python3
import sys
class fasta():
    def __init__(self,input,output):
        self.input=input
        self.output=output
    def read(self):
        f = open(self.input,"r")
        dict_seq={}
        seq=""
        for line in f:
            if line.startswith(">"):
                if seq != "":
                    dict_seq[seq_id] = seq
                    seq =""
                seq_id = line.rstrip("\n")
            else:
                seq = seq + line.rstrip("\n")
        dict_seq[seq_id]=seq
        f.close()
        return dict_seq
results = fasta(sys.argv[1],sys.argv[2])
print(results.read())