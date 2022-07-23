#!/usr/bin/env python3
file = open("/home/dylan/Documents/Other/Rosalind/Complementing_a_Strand_of_DNA/rosalind_revc.txt")
data = file.read()
data=data.replace("T", "a").replace("A", "t").replace("C", "g").replace("G", "c").upper()
data=data[::-1]
print (data)
