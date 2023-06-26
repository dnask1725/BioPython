#Enter pre-mRNA input and perform post translational modifications such as Poly_A adenylation and 5'-capping(methylation)

mRNA=("augccaugcaucgauaauugcaa ").upper()

new_mRNA="MET"+ mRNA + "AAAAAAAA"
print(new_mRNA)
