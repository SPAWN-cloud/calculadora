#-- coding: UTF-8 --

#--NAO KIBA CARALHOKKKKKK--#

import time

verm = '\033[1;91m'
ama = '\033[1;93m'
verd = '\033[1;92m'

while True:
    print(f'''
   {verm}
           _            _           _                 
          | |          | |         | |                
  ___ __ _| | ___ _   _| | __ _  __| | ___  _ __ __ _ 
 / __/ _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |
| (_| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
 \___\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|
                                                      
                $coded by spawnDEV                                
    
    
    
    ''')
    SOM = int(input(f''' {verd}
    Digite: 
    [1] para somar
    [2] para multiplicar 
    [3] para diminuir
    [4] para dividir

    [#]: '''))

    if SOM == 1:
        Count = int(input('Qual é o numero? '))
        Count1 = int(input('Qual é o numero? '))
        Sum = Count1 + Count
        print('Resposta da Conta:',Sum)

    elif SOM == 2:
        Couting = int(input('Qual é o numero? '))
        Couting1 = int(input('Qual é o numero? '))
        Multiply = Couting1 * Couting
        print('Resposta da Conta:',Multiply)

    elif SOM == 3:
        MinusCount1 = int(input('Qual é o numero? '))
        MinusCount2 = int(input('Qual é o numero? '))
        Minus = MinusCount1 - MinusCount2
        print('Resposta da Conta:',Minus)

    elif SOM == 4: 
        Divid1 = int(input('Qual é o numero? '))
        Divid2 = int(input('Qual é o numero? '))
        Divid = Divid1 / Divid2
        print('Resposta da Conta:',Divid)

    else: print('Resposta Iválida')
    time.sleep(1)
#--NAO KIBA $ 'spawnDEV'--#
