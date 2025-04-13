anos=int(input("Qual ano voce quer saber se eh bisexto? "))
Zero=str(anos)
if (Zero[3]==0 and Zero[2]==0 and (Zero/400)==0 ) or (anos%4)==0:
    print("O ano {} eh bisexto!!".format(anos))
else:
    print("O ano {} nao eh bisexto".format(anos))