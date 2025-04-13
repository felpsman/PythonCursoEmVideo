lado1=int(input("Digite o primeiro lado do triangulo: "))
lado2=int(input("Digite o segundo lado do triangulo: "))
lado3=int(input("Digite o terceiro lado do triangulo: "))
possivel=(lado1>(lado2+lado3) or lado2>(lado3 + lado1) or lado3<(lado1+lado2))
equilatero=(lado1==lado2==lado3)
escaleno=(lado1!=lado2 and lado2!=lado3 and lado1!=lado3)
isoceles=(lado1==lado2 or lado2==lado3 or lado1==lado3)
if possivel==True:
    print("Eh possivel formar um triangulo!")
if(possivel==True and equilatero==True):
    print("Equilatero")
elif(possivel==True and escaleno==True):
    print("Escaleno!")
elif(possivel==True and isoceles==True):
    print("Isoceles")
else:
    print("Nao pode formar um triangulo!")
