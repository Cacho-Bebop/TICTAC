def validation(field, filled_fields):

        """Validacion de que el campo seleccionado no pertenezca a los campos ya llenos"""

        for num in filled_fields:
            
            if ( int(field) == int(num) ):
                    
                    return False
        
        return True
                     
def inp_f(turn, filled_fields):
    
    """funcion encargada de recibir el campo a rellenar, corroborar que sea valida y retornarla"""
        
    # mostramos de quien es el turno
    print(f"Is turn of the player {turn}")
    
    checker = False # flag -> True if the validation is successfull
    
    
    while checker == False:
        
        # muestra informacion necesaria
        inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n->")
        
        # verificacion de que el dato pasado sea un digito 
        while inp.isdigit() == False:
            
            inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n-> ")
        
        
        checker = validation(inp, filled_fields)

        if checker == False:
            print("\nPorfavor selecciona un casillero valido.")

  
        # Una vez verificada la validez de la seleccion, devolverla

    if checker == True:
        return int(inp)
       
ff = [5,4,1]
turn = 1

print(inp_f(turn, ff))