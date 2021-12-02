from random import randint, random, seed
seed(101)
def validation(field, filled_fields):

        """Validacion de que el campo seleccionado no pertenezca a los campos ya llenos"""

        for num in filled_fields:
            
            if ( int(field) == int(num) ) or (num >= 10) or (num < 0):
                    
                    return False
        
        return True
                     
def inp_f(turn, filled_fields):
    

    """funcion encargada de recibir el campo a rellenar, corroborar que sea valida y retornarla"""
        
    # mostramos de quien es el turno
    print(f"Turno de jugador {turn}.")
    
    checker = False # flag -> True if the validation is successful
    
    
    while checker == False:
        
        # muestra informacion necesaria
        inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n->")
        
        
                
        # verificacion de que el dato pasado sea un digito 
        while inp.isdigit() == False:
            
            inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n-> ")
        
        if int(inp) < 1:
           
           inp = randint(1,8)
        
          
        checker = validation(inp, filled_fields)

        if checker == False:
            print("\nPorfavor selecciona un casillero valido.")

  
        # Una vez verificada la validez de la seleccion, devolverla

    if checker == True:
        return int(inp)