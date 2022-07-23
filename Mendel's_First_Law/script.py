#!/usr/bin/env python3
import sys
class fasta():
    def __init__(self, input, output):
        self.input=input
        self.output=output
    def read(self):
        """
        Read a single line
        """
        f = open(self.input,"r")
        list_input = f.readline().rstrip("\n").split(" ")
        return (int(list_input[0]),int(list_input[1]),int(list_input[2]))
    def probability(self):
        (k,m,n) = fasta.read(self)
        prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*(k+m+n)*((k+m+n)-1))
        return prob
    def write(self):
        f=open(self.output,"w")
        prob = fasta.probability(self)
        f.write("%.5f" %prob)
        f.close()
results = fasta(sys.argv[1],sys.argv[2])
print(results.read())
print(results.probability())
results.write()