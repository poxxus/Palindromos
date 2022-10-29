Pal = int(input("Insira um número de 1 a 99: "))
if Pal<10:
  print("O número é um palíndromo")
elif 10<Pal<99:
  if Pal%11==0:
    print("O número é um palíndromo")
  else:
    print("O número não é um palíndromo")
