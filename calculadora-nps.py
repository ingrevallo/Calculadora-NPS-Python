# -*- coding: utf-8 -*-
"""
Esta calculadora NPS funciona da seguinte maneira:
Você insere na calculadora a quantidade recebida de cada nota na escal de 0 a 10
e a calculadora automaticamente vai mostrar:
- Clientes Detratores
- Clientes Neutros
- Clientes Promotor
- Valor NPS
O valor do NPS é calculado da seguinte maneira:
NPS = Percentual de Clientes Promotores (notas 9 e 10) - Percentual de Detratores (notas de 0 a 6)
(clientes neutros não entram no cálculo)
Exemplo:
- 40% dos clientes são promotores (deram notas 9 ou 10)
- 5% dos clientes são detratores (deram notas entre 0 e 6)
- 55% dos clientes são neutros (deram notas 7 ou 8)
- NPS = 40% – 5% = 35 (o número é apresentado sem o percentual
"""

#notas_nps = {0:"detrator", 1:"detrator", 2:"detrator", 3:"detrator", 4:"detrator", 5:"detrator",6:"detrator", 7:"neutro", 8:"neutro", 9:"promotor", 10:"promotor"}
#print(notas_nps)

nota_zero = int(input('Digita a quantidade recebida de notas Zero: '))
nota_01 = int(input('Digita a quantidade recebida de notas "1" '))
nota_02 = int(input('Digita a quantidade recebida de notas "2" '))
nota_03 = int(input('Digita a quantidade recebida de notas "3" '))
nota_04 = int(input('Digita a quantidade recebida de notas "4" '))
nota_05 = int(input('Digita a quantidade recebida de notas "5" '))
nota_06 = int(input('Digita a quantidade recebida de notas "6" '))
nota_07 = int(input('Digita a quantidade recebida de notas "7" '))
nota_08 = int(input('Digita a quantidade recebida de notas "8" '))
nota_09 = int(input('Digita a quantidade recebida de notas "9" '))
nota_10 = int(input('Digita a quantidade recebida de notas "10" '))

detratores = nota_zero + nota_01 + nota_02 + nota_03 + nota_04 + nota_05 + nota_06
neutros = nota_07 + nota_08
promotores = nota_09 + nota_10

total_de_notas = detratores + neutros + promotores

percentual_detratores = (detratores/total_de_notas)*100
percentual_neutros = (neutros/total_de_notas)*100
percentual_promotores = (promotores/total_de_notas)*100

nps = percentual_promotores - percentual_detratores

print(str("A quantidade total de Detratores é: ") + str(detratores) + str(" - ")+ str(round(percentual_detratores,2)) + str("% das notas recebidas"))
print(str("A quantidade total de Neutros é: ") + str(neutros) + str(" - ")+ str(round(percentual_neutros, 2)) + str("% das notas recebidas"))
print(str("A quantidade total de Promotores é: ") + str(promotores) + str(" - ")+ str(round(percentual_promotores, 2)) + str("% das notas recebidas"))

print(str("O seu NPS é: ") + str(round(nps, 2)))