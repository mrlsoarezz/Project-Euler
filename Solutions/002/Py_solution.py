n1 = 1
n2 = 2
aux = n2
sum = 0

while n1 < 4000000:
    n1 = n1 + aux
    if (n1 % 2 == 0):
        sum += n1
        print(sum)
    aux, n2 = n2, n1
