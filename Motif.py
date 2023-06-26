#Protein sequence motifs are signature of protein families and are used often as tools for protein structure prediction.
#They may or may not be defined by unique biological or chemical function
#Presence of Motif
#Index function used


prot=("MTIPFGVTPKMMLIT")
#prot=("Enter the protein sequence: ").upper()
motif=("GVTP")
#motif=("Enter the motif : ").upper()
if(motif in prot):
    loc=prot.index(motif)
    print("MOTIF FOUND AT LOCATION: ",loc)
else:
    print("Opsiee not present")
