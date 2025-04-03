#Entradas
N = int(input(""))
Contador = 0
ContadorIn = 0
ContadorOut = 0
#Caja negra
while (Contador<N):
    X = int(input(""))
    Contador = Contador+1
    if (10<=X<=20):
        ContadorIn = ContadorOut + 1
    elif (10>X or X>20):
        ContadorOut = ContadorOut + 1

print(f"{ContadorIn} in")
print(f"{ContadorOut} out")