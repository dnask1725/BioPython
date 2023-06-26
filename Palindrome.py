my_seq=("AGTATCTGGAACTNGCNCAATATGCACTACTATACCTGACTCTGTGGCAGGNCCCTTGTGGT").upper()
rev_seq=reversed(my_seq)
if rev_seq==my_seq:
    print("It is a palindrome")
else:
    print("It is not")
