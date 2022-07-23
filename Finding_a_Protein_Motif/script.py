#!/usr/bin/env python3
import sys
import requests
import re

class fasta():
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def get_ids(self):
        f = open(self.input,"r")
        string = []
        for line in f:
            #id_prot = str(((line.rstrip("\n")).split("_"))[0]) # uniprotid_abc_efg -> uniprotid
            id_prot = line.rstrip("\n")
            string.append(id_prot)
        return string
    def get_fasta(self):
        url = 'https://www.uniprot.org/uniprot/'
        sequences = {}
        seq_id = fasta.get_ids(self)
        id_prot = ""
        for prot_id in seq_id:
            id_prot = str(((prot_id).split("_"))[0]) # uniprotid_abc_efg -> uniprotid
            goToURL = url+id_prot+".fasta"
            response = requests.get(goToURL)
            seq_prot = ""
            seq_prot = response.text.split("\n") # convert to list
            seq_prot = "".join(seq_prot[1:])        # join list
            sequences[prot_id] = seq_prot
        return(sequences)
    def find_motif(self):
        """
        Find N-glycosylation motif.
        To allow for the presence of its varying forms, a protein motif is 
        represented by a shorthand as follows: [XY] means "either X or Y" 
        and {X} means "any amino acid except X." For example, the N-glycosylation 
        motif is written as N{P}[ST]{P}.
        """
        sequences = fasta.get_fasta(self)
        dict_pos = {}
        for key,value in sequences.items():
            dict_pos.setdefault(key, [])
            for i in range(0,len(value)-3):
                seq = value[i:i+4]
                if (seq[0] == "N") & (seq[1] != "P") & (seq[2] == "S" \
                    or seq[2] == "T") & (seq[3] != "P"):
                    dict_pos[key].append(i+1)
        return(dict_pos)
    
    def write_file(self):
        f = open(self.output,"w")
        dict_pos = fasta.find_motif(self)
        i = 0
        for key in dict_pos.keys():
            if len(dict_pos[key]) != 0:
                if i == 0:
                    f.write("%s\n" %key)
                else:    
                    f.write("\n%s\n" %key)
                for value in dict_pos[key]:
                    f.write("%s " %value) 
                i+=1

try:
    result = fasta(sys.argv[1],sys.argv[2])
    result.write_file()
except:
    print("Error!!! Try:\n ./script.py input.file output.file")