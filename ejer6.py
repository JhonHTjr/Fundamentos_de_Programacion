n=int(0)
ni=int(0)
r=int(0)

n=int(input("ingresee el numero: "));

r=int(n%10)
n=int(n/10)
ni=int(r*10)
print (" r: ",r)
print (" n: ",n)
print (" ni: ",ni)

r=int(n%10)
n=int(n/10)
ni=int((ni+r)*10)
print (" r: ",r)
print (" n: ",n)
print (" ni: ",ni)

r=int(n%10)
n=int(n/10)
ni=int((ni+r)*10)
print (" r: ",r)
print (" n: ",n)
print (" ni: ",ni)

r=int(n%10)
n=int(n/10)
ni=int((ni+r)*10)
print (" r: ",r)
print (" n: ",n)
print (" ni: ",ni)



ni=int(ni+n)

print ("este es la respuesta",ni)
