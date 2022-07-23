#!/usr/bin/env python3

import sys
import rna_prot
class fasta():
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def read_file(self):
        f = open(self.input,"r")
        list_lines=[]
        string_seq = ""
        #list_lines = f.readlines()
        #list_lines = [string.rstrip("\n") for string in list_lines]
        for line in f:
            if line.startswith(">"):
                if string_seq != "":
                    list_lines.append(string_seq)
                string_seq = ""
                list_lines.append(line.rstrip("\n"))
            else:
                string_seq= string_seq + line.rstrip("\n")
        list_lines.append(string_seq)
        return list_lines
    def rna_splice(self):
        list_lines = fasta.read_file(self)
        seq = list_lines[1]
        intron_list=[]
        for i in range(3,len(list_lines),2):
            intron_list.append(list_lines[i])
        for string in intron_list:
            seq = seq.replace(string,"")
        seq = seq.replace("T","U")
        return seq
    def translate(self):
        seq = fasta.rna_splice(self)
        dict = rna_prot.dict_rna_prot
        prot_seq = ""
        for i in range(0, len(seq)-2,3):
            if dict[seq[i:i+3]] != "Stop":
                prot_seq = prot_seq + dict[seq[i:i+3]]
        return(prot_seq)
    def write(self):
        f = open(self.output,"w")
        prot_seq = fasta.translate(self)
        f.write(prot_seq)
        
results = fasta(sys.argv[1],sys.argv[2])    
results.write()