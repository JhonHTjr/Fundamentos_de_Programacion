a=int
b=int
c=int
a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
c=int(input("ingrese un numero: "))
if a != b and a !=c and b !=c:
    if a > b:
        if a > c:
            print("el numero amyor es: ",a)
        else:
            print("el numero mayor es: ",c)
    else:
        if b > c:
            print("el numero mayor es: ",b)
        else:
            print("el numero mayor es: ",c)
else:
    print("ingresa 3 numeros diferentes")