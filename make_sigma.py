import sys,os
import random

lines = open(sys.argv[1],"r").readlines()
ofile = open(sys.argv[2],"w")

for line in lines:
    cols = line.split()
    h=int(cols[0])
    k=int(cols[1])
    l=int(cols[2])
    f=float(cols[3])
    p=float(cols[4])

    sigf=float(random.random())

    ofile.write("%4d%4d%4d%12.3f%12.3f%12.3f\n"%(h,k,l,f,sigf,p))

