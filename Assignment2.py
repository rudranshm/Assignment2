p1=input("Probability of first student solving the problem (in x/y form)  : ")
p2=input("Probability of second student solving the problem (in x/y form) : ")
p3=input("Probability of third student solving the problem (in x/y form)  : ")

P1=int(p1[0])/int(p1[2])
P2=int(p2[0])/int(p2[2])
P3=int(p3[0])/int(p3[2])

notp1 = 1-P1
notp2 = 1-P2
notp3 = 1-P3

notall = notp1 * notp2 * notp3

solvedp = 1 - notall

print("The probability of the problem getting getting solved : ", solvedp)