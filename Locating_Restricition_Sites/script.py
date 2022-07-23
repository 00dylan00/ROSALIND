#!/usr/bin/env python3
import sys

class fasta():
    def __init__(self, input_file, output_file):
        self.input = input_file
        self.output= output_file
    def read(self):
        """
        Read file & return FASTA sequence 
        ONLY for SINGLE FASTA input
        """
        f = open(self.input,"r")
        sequence =""
        for line in f:
            if not line.startswith(">"):
                sequence = sequence + line.rstrip("\n") 
        return sequence
    def comp_rev(string):
        return string.replace("T", "a").replace("A", "t").replace("C", "g").replace("G", "c").upper()[::-1]                
    def palindrome(self):
        """
        search for palindrome position & length
        """
        seq = fasta.read(self)
        dict_palindrome = {}
        for i in range(len(seq)):
            for n in range(4,13):
                print(seq[i:i+n])
                print(fasta.comp_rev(seq[i:i+n]))
                if seq[i:i+n] == fasta.comp_rev(seq[i:i+n]) and len(seq[i:i+n][::-1]) == n:
                    if i+1 not in dict_palindrome:
                        dict_palindrome[i+1] = list()
                        dict_palindrome[i+1].append(n)
                    else:
                        dict_palindrome[i+1].append(n)
        return dict_palindrome
    def write_file(self):
        f = open(self.output,"w")
        dict_pal = fasta.palindrome(self)
        for key,list in dict_pal.items():
            for value in list:
                f.write("%d %d\n"%(key,value))

results = fasta(sys.argv[1], sys.argv[2])
print(results.palindrome())
results.write_file()