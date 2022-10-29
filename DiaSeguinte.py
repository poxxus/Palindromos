dia, mes, ano = input(), input(), input()
dia, mes, ano = [int(x) for x in [dia, mes, ano]]
dia = dia + 1
if mes in (1,3,5,7,8,10,12) and dia > 31:
   dia = 1
   mes = mes + 1
   if mes > 12:
     mes = 1
     ano = ano + 1
if mes == 2:
    if ano%4==0 and ano%100!=0 or ano%400==0:
        if dia > 29:
          dia = 1
          mes = mes + 1
    else:
        if dia > 28:
         dia = 1
         mes = mes + 1
if mes in (4,6,9,11) and dia > 30:
        dia = 1
        mes = mes + 1
print(dia,mes,ano)