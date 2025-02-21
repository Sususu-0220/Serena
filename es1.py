a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))

if a >= b and a >= c:
    print(a)
    print("e' il numero piu' grande")
elif b >= a and b >= c:
    print(b)
    print("e' il numero piu' grande")
elif c >= a and c >= b:
    print(c)
    print("e' il numero piu' grande")

