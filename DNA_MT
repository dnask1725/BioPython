#It is the temp. in which the oligonucleotides are half single stranded and half are double stranded.
#Basic formula is Tm= (wA+xT)*2+ (yG+zC)*4.  where w,x,y,z are number of bases A,T,G,C in the sequence
#there is a linear relationship between the amount of guanine and cytosine in a given DNA molecule, known as the GC content and the temperature at which the double helix will denature, called the melting point

from Bio.SeqUtils import MeltingTemp as mt
seq=("ACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAGTTTTACATTCAACTCAGGACTTGTTCTTACCTTTCTTTTCCAATGTTACTTGGTTCCATGCTATACATGTCTCTGGGACCAATGGTACTAAGAGGTTTGATAACCCTGTCCTACCATTTAATGATGGTGTTTATTTTGCTTCCATGAGAGTCTAACATAATAAGAGGCTGGATTTTTGGTACTACTTTAGATTCGAAGACCCAGTCCCTACTTATTGTTAATAACGCTACTAATGTTGTTATTAAAGTCTGTGAATTTCAATTTTGTAATGATCCATTT")
size=len(seq)   #to calculate total number of A,T,G,C

g_count=seq.count("G")
c_count=seq.count("C")

total_GC = g_count + c_count

GC_content= (total_GC/size)*100
print("The GC Content is : ",GC_content)

#for melting temperature
print('%0.2f' % mt.Tm_GC(seq))


#alternate method
from Bio.SeqUtils import MeltingTemp
seq=("ACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAGTTTTACATTCAACTCAGGACTTGTTCTTACCTTTCTTTTCCAATGTTACTTGGTTCCATGCTATACATGTCTCTGGGACCAATGGTACTAAGAGGTTTGATAACCCTGTCCTACCATTTAATGATGGTGTTTATTTTGCTTCCATGAGAGTCTAACATAATAAGAGGCTGGATTTTTGGTACTACTTTAGATTCGAAGACCCAGTCCCTACTTATTGTTAATAACGCTACTAATGTTGTTATTAAAGTCTGTGAATTTCAATTTTGTAATGATCCATTT")
print(MeltingTemp.Tm_GC(seq))
