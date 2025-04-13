lado1=int(input())
lado2=int(input())
lado3=int(input())
if lado1 > (lado2+lado3) and lado2>(lado3 + lado1) and lado3<(lado1+lado2):
    print("Eh possivel formar um triangulo!")
else:
    print("Nao pode formar um triangulo!")
