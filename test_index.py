lista = [1,5,9]

def testing(lista):
    
    x = ''
    indexes = list( '' for x in range (9) )
    
    for num in lista:
        
        indexes[int(num) - 1]    =   'X'
    
    print(indexes)


testing(lista)       
        