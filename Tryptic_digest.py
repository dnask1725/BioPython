#collect amino acid sequence from user (list) and perform tryptic digest and convert the result into string
#cleavage rule for trypsin :  after R or k, but not before P(i.e the trypsin cleaves (cuts) the protein sequence after each K or R, unless (K or R) is followed by a P)-all of this in a protein

prot=["A","T","G","K","P","A","R","Q","A"]
for i in range (0, len(prot)):
    if prot[i]=='K'or prot[i]=='R':
        if prot[i+1]!='P':
            prot.insert(i+1," ")
str1=""
trypsin=str1.join(prot)
print("The trypsin cleavage :",trypsin)

#here K was followed by P so it did not cleave but R was not followed by P , so it cleaved.
