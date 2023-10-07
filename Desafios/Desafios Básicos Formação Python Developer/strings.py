"""
Desafio
Paulinho tem em suas mãos um novo problema. 
Agora a sua professora lhe pediu que construísse um programa para verificar, 
à partir de dois valores muito grandes A e B, 
se B corresponde aos últimos dígitos de A.
"""
qt = int(input())

v = []


for i in range(qt):

  v = input().split(" ")

  a = v[0]

  b = v[1]


  if len(b) > len(a):

    print("nao encaixa")

  elif a.endswith(b):

    print("encaixa")

  else:

    print("nao encaixa")  