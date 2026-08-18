# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
from datetime import date

ano = int(input('Digite um Ano que voce quer analisar, ou digite 0 para selecionar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 400 == 0:
    print('O Ano que voce digitou é Bissexto')
else:
    print('O Ano que voce digitou não é Bissexto')