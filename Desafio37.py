print('''Digite um numero e escolhe pra qual base o numero sera convertido:
         [1] Binario
         [2] Octal
         [3]Hexadecimal''')
opcao=int(input("Qual opcao de conversao sera escolhida? "))
num=int(input("Digite um numero para converter para a base escolida: "))
#A conversao sera feita de acordo com a opcao escolhida.
if(opcao==1):
    print("O numero {} em binario eh: {}".format(num,bin(num)[2:]))
elif(opcao==2):
    print("O numero {} em octal eh: {}".format(num,oct(num)[2:])) #Usando a funcao de conversao. Colocando espacamento para nao aparecer o que singinifca a conversao
elif(opcao==3):
    print("O numero {} em hexadecimal eh {}".format(num,hex(num)[2:]))
else:
    print("Escolha uma forma de Conversao Valida!")
