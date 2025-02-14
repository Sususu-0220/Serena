a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)