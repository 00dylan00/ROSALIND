#!/usr/bin/env python3
file = open("/home/dylan/Documents/Other/Rosalind/Transcribing_DNA_into_RNA/rosalind_rna.txt")
data = file.read()
data=data.replace("T", "U")
print (data)
