def nps(nota_zero, nota_01, nota_02, nota_03, nota_04, nota_05, nota_06, nota_07, nota_08, nota_09, nota_10):
    detratores = nota_zero + nota_01 + nota_02 + nota_03 + nota_04 + nota_05 + nota_06
    neutros = nota_07 + nota_08
    promotores = nota_09 + nota_10
    total_de_notas = detratores + neutros + promotores
    percentual_detratores = (detratores/total_de_notas)*100
    percentual_neutros = (neutros/total_de_notas)*100
    percentual_promotores = (promotores/total_de_notas)*100
    nps = (round((percentual_promotores - percentual_detratores), 2))
    return nps