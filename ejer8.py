t=int
c=str

t=int(input("ingrese temperatura: "))

if t<10:
    c="frio"
    print(c)
else:
    if t >=10 & t <=20:
        c="nublado"
    if  t>=25:
        c="trpical"
print(c) 