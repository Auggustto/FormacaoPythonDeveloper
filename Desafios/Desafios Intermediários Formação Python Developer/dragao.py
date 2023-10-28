''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
C = int(input()) 
for i in range(C): 
    ''' 
    todo Leia as as entradas e crie as condições necessárias para verificar se é maior ou
    menor do que 8000 e imprima "Inseto!" ou "Maior que 8000!" para cada caso.
    '''
    if i == C:
        break
    else:
        N = int(input())
        
        if N <= 8000:
            print("Inseto!")
        else:
            print("Mais de 8000!")
    