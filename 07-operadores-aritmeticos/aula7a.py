n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s} \n a mutiplicação é {m} \n a divisão é {d:.3f} \n a divisão inteira é {di} \n e a potência é {e}')

#       \n -> nova linha
#       Dentro dos {:.3f} para demilitar a quantidade de casas decimais flutuantes
#       No final pode colocar (, end=' ') para juntar com a outra linha
