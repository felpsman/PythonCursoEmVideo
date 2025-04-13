nascimento=int(input("Qual o seu ano de nascimento? "))
categoria=2025-nascimento
if(categoria<=9):
    print("Mirim")
elif(categoria>9 and categoria<=14):
    print("Infantil")
elif(categoria>14 and categoria<=19):
    print("Junior")
elif(categoria==20):
    print("Senior!")
else:
    print("Master")