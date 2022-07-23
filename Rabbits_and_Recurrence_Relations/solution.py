#!/usr/bin/env python3
file = open("/home/dylan/Documents/Other/Rosalind/Rabbits_and_Recurrence_Relations/rosalind_fib.txt")
data = file.read()
data = data.rstrip().split(' ')
#print (data[0])
if (int(data[0]) == 1):
	print (1)
elif (int(data[0]) == 2):
	print (data[1])
else:
	gen_a=1
	gen_b=1
	value=0
	for i in range(2, int(data[0])):
		value = gen_a + int(data[1])*gen_b
		gen_b=gen_a
		gen_a= value
	print (value)


