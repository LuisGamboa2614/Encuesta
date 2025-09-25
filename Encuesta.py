print("=== ENCUESTA ESTUDIANTES ===")
c=0
i=10
d=""
while i>=0:
    a=input("¿Cual es tu nombre? ")
    b=input("¿Que idea de proyecto tienes? ")
    c=a+"   "+b
    d=d+";"+c
    i=i-1
print(f"Sus nombres y respectivas ideas de proyecto son: {d}")