# -*- coding: utf-8 -*-

import nps_function

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

calcular_nps = nps_function.nps(nota_zero, nota_01, nota_02, nota_03, nota_04, nota_05, nota_06, nota_07, nota_08, nota_09, nota_10)

print(str(f"O seu NPS é: {calcular_nps}"))
