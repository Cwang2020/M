n = int(input("Enter the length of the sequence: ")) # Do not change this line

a1 = 0
a2 = 0
a3 = 1

for a in range (0, n):
    if a3 < 2:
        sum = a1 + a2 + a3
        a2 = a3
        a3 = sum 
    else:
        sum = a1 + a2 + a3
        a1 = a2
        a2 = a3
        a3 = sum
    print(sum)
        
