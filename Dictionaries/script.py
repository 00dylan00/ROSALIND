#!/usr/bin/env python3
import sys
class fasta():
    def __init__(self,input,output):
        self.input=input
        self.output=output
    def read_file(self):
        f = open(self.input,"r")
        text = ""
        for line in f:
            text = text + line.rstrip("\n")
        return text.split(" ")
    def dictionary(self):
        list_txt = fasta.read_file(self)
        dict_txt = {}
        for element in list_txt:
            if element in dict_txt:
                dict_txt[element] +=1
            else:
                dict_txt[element]=1
        return dict_txt
    def write(self):
        f = open(self.output,"w")
        dict_txt = fasta.dictionary(self)
        for key,value in dict_txt.items():
            f.write("%s %d\n"%(key,value))
        f.close()
results = fasta(sys.argv[1],sys.argv[2])
print(results.read_file())
print(results.dictionary())
results.write()