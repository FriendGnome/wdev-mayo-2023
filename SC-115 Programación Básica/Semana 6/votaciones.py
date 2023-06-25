print("Bienvenidos a las elecciones de GoP")

candidatos=4

candidato1=0
candidato2=0
candidato3=0
candidato4=0
ganador=0

voto_nulo=0

total_votos=0


nombre_candidato1= input("digite nombre del pimer candidato")
nombre_candidato2= input("digite nombre del segundo candidato")
nombre_candidato3= input("digite nombre del tercer candidato")
nombre_candidato4= input("digite nombre del cuarto candidato")

voto= input("Ingrese el cantidato de su preferencia o digite salir")

while voto !="salir":
    if voto ==nombre_candidato1:
        candidato1+=1
    elif voto ==nombre_candidato2:
        candidato2+=1
    elif voto ==nombre_candidato3:
        candidato3+=1
    elif voto ==nombre_candidato4:
        candidato4+=1
    else: 
        voto_nulo+=1
    
if candidato1>candidato2:
    if candidato1>candidato3:
        if candidato1>candidato4:
            ganador=nombre_candidato1
        else:
            ganador=nombre_candidato4
    elif candidato3>candidato4:
        ganador=nombre_candidato3
    else:
        ganador=nombre_candidato4
elif candidato2>candidato3:
    if candidato2>candidato4:
        ganador=nombre_candidato2
    else:
        ganador=nombre_candidato4
elif candidato3>candidato4:
    ganador=nombre_candidato3
else:
    ganador=nombre_candidato4

total_votos=candidato1+candidato2+candidato3+candidato4+voto_nulo
print("Total de votos:",total_votos)

print("Resultados: el ganador es", ganador)
print(nombre_candidato1)
print("cantidad de votos:", candidato1)
print(nombre_candidato2)
print("cantidad de votos:", candidato2)
print(nombre_candidato3)
print("cantidad de votos:", candidato3)
print(nombre_candidato4)
print("cantidad de votos:", candidato4)
print("votos nulos")
print("cantidad:", voto_nulo)