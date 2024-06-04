#IMC
while 
peso=int(input("Ingrese el peso de la persona: "))
altura=str(input("Ingrese la altura de la persona: "))

imc=peso /(altura*altura)
print=input(imc)

if imc<18.5:
    print=("Peso inferior al normal")
if imc>=18.5 and imc<=24.9:
    print("Peso normal")
if imc>=25.0 and imc<=29.9:
    print("Peso superior al normal")
if imc>30:
    print("Obesidad")

