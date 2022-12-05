def sumaDigitos(num):
    s = 0
    while num > 0:
        s = s + num % 10
        num = num // 10
    return s

n = int(input("Ingrese cantidad de numeros enteros: "))
suma = 0
while n > 0:
    
    num = int(input("Numero: "))
    suma = suma + sumaDigitos(num)
    n = n - 1
    
print(suma)
