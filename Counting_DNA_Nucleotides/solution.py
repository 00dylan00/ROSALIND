#!/usr/bin/env python3
#data ='ACCCCTTTTTTTTGGGGGGGG'
file = open("/home/dylan/Documents/Other/Rosalind/Counting_DNA_Nucleotides/rosalind_dna.txt")
data = file.read()
#print (data)
#import re
count_A = 0
count_T = 0
count_C = 0
count_G = 0
for i in range(0, len(data)):
	if data[i] == 'A':
		count_A += 1
	if data[i] == 'T':
		count_T += 1
	if data[i] == 'C':
		count_C += 1
	if data[i] == 'G':
		count_G += 1
print(count_A, count_C, count_G, count_T)


## EOF ###

#data = readstring(file)
#close(file)

#symbol = 'ACGT'

#for i in symbol
#	print (sequence.count(i), end = " ")

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
#	print(x, end = " ")

#fruit = "apple"
#for x in fruit:
#	print(fruit.count(x), end = " ")


#file = open("/home/dylan/Documents/Other/Rosalind/Counting_DNA_Nucleotides/TEST")
#data = readstring(file)
#close(file)
