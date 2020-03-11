#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Valor da coca é 45 centavos
#Só é possivel inserir moedas de 25 e 10
#Não devolve moedas Inseridas

coca = 0.45
valor = 0.0

print("\n\n---Preço da Coca é : 45 centavos---")
print("---Insira os valores em centavos---\n\n")


while(valor<coca):

moeda= float(input('Insira uma moeda\n\t'))
moeda /= 100

if (moeda==0.25) or (moeda==0.1):
valor += moeda
round(valor,2)
print("\n\nValor já inserido:", round(valor,2))

else:
print("\n----Só aceitamos moedas equivalente a 25 e 10 centavos---")
print("---Você perdeu seu dinheiro!---\n\n")

if (valor==0.45):
print("\n\n\n\t\tPARABENS!!! Você adquiriu uma coca por 45 centavos")
else:
print("\n\n\n\t\tVocê adquiriu sua coca por %s reais. Não devolveremos seu troco!"% valor)
