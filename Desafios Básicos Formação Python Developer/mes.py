""" 
Desafio
Leia um valor inteiro entre 1 e 12, inclusive. 
Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, 
em inglês, com a primeira letra maiúscula.
"""

month = int(input("Enter the month number: \n"))

months_dict = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

if month in months_dict:
    print(f"the number: {month} refers to the month: {months_dict[month]}.")
else:
    print("please enter a valid month!")

