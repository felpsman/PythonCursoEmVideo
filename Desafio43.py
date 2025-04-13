altura=float(input("Qual a sua altura? "))
Peso=float(input("Quantos kilos voce tem? "))
IMC=Peso/(altura*altura)
if(IMC<18.5):
    print("Abaixo do peso!")
elif(IMC>=18.5 and IMC<=25.0):
    print("Peso Ideal!")
elif(IMC>25.0 and IMC<=30.0):
    print("Sobre Peso!")
elif(IMC>30 and IMC<=40.0):
    print("Obeso")
else:
    print("Obesidade Morbida")