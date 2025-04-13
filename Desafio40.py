nota1=float(input("Qual foi a sua primeira nota? "))
nota2=float(input("Qual foi a sua segunda nota? "))
media=(nota1+nota2)/2.0
if(media<5.0):
    print("O aluno foi reprovado!")
elif(media>=5.0 and media<=6.9):
    print("O aluno esta de recuperacao!")
else:
    print("O aluno foi aprovado!")