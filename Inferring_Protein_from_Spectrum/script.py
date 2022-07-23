#!/usr/bin/env python3

import sys

from sqlalchemy import values
import sequence_data

class fasta():
    def __init__(self, input, output):
        self.input=input
        self.output=output
    def read(self):
        f = open(self.input,"r")
        mw_value=0
        mw_diff=[]
        for line in f:
            if mw_value != 0:
                mw_diff.insert(0,abs(mw_value - float(line.rstrip("\n"))))            
            mw_value=float(line.rstrip("\n"))
        f.close
        return mw_diff
    def identify_aa(self):
        dict_mw = sequence_data.dict_mw
        list_mw = fasta.read(self)
        sequence_aa=""
        for number in list_mw:
            for key,value in dict_mw.items():
                if round(value,2) == round(number,2):
                    sequence_aa=key+sequence_aa
        return(sequence_aa)
    def write(self):
        f = open(self.output,"w")
        f.write(str(fasta.identify_aa(self)))
        f.close
result_mw = fasta(sys.argv[1], sys.argv[2])
print(result_mw.read())
print(result_mw.identify_aa())
result_mw.write()