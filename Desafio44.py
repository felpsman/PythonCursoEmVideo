preco=int(input("Qual eh o valor total da compra? R$"))
opcao=int(input('''Qual sera a opcao de pagamento escolhida?
                [1] A vista no dinheiro/cheque
                [2] A vista no cartao de credito
                [3] 2x no cartao
                [4] 3x ou mais no cartao
                Opcao escolhida: '''))
if(opcao==1):
    print("Boa escolha, voce tera um desconto de 10%, com isso o valor total ficara de R${:.2f}".format(preco-(preco*0.10)))
elif(opcao==2):
    print("Boa escolha, voce tera um desconto de 5%, com isso o valor total a ser pago sera : R${:.2f}".format(preco-(preco*0.05)))
elif(opcao==3):
    print("Boa escolha, assim voce tera mais tempo para pagar. O valor total eh R${} , sendo assim, ficara R${:.2f} por mes.".format(preco,preco/2))
elif(opcao==4):
    precojuros=preco+(preco*0.20)
    parcela=int(input("Voce tera que pagar juros. Em quantas vezes voce ira querer pagar? "))
    print("O valor total com juros, sera de: R${}, sendo assim, cada parcela saira por: R${:.2f}".format(precojuros,precojuros/parcela))
else:
    print("Escolha uma forma de pagamento valida!")
