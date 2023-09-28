"""
Desafio
Paulinho tem em suas mãos um novo problema. 
Agora a sua professora lhe pediu que construísse um programa para verificar, 
à partir de dois valores muito grandes A e B, 
se B corresponde aos últimos dígitos de A.
"""

N = int(input("Enter the comparison quantity: \n"))

A = input("Enter the number for [A]: \n")
B = input("Enter the number for [B]: \n")

while(N > 0):

    if B[-3:] == A[-3:]:
        print("fits!")
        break
        
    else:
        print("Does not fit!")
        break