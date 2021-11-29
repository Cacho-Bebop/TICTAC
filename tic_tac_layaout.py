from math import trunc
from random import randint

def display_tictac_layout():
    
    row1 = [7,8,9]
    row2 = [4,5,6]
    row3 = [1,2,3]
    
    print(f"{row1}\n{row2}\n{row3}")

display_tictac_layout()

def playing():
    
    """The game running"""
    keep_playing = True
    
    ### input of the players 
    inp_p1 = 0
    inp_p2 = 0
    
    turn   = 1
    
    fields = [1,2,3,4,5,6,7,8,9] # structure index based 
    filled_fields = []
    
    while keep_playing:
        
        # turn based input:
        if turn == 1:
            pass
      
def validation(field, filled_fields):

        """Validacion de que el campo seleccionado no pertenezca a los campos ya llenos"""

        if field in filled_fields:
            
            return False
        
        else:
            
            return True
                     
def manage_turn(turn, filled_fields):
    
    """funcion encargada de manejar el turno / recibir entrada / corroborar que sea valida"""
        
    # mostramos de quien es el turno
    print(f"Is turn of the player {turn}")
    
    while True:
        
        # muestra informacion necesaria
        inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n -> con 0 numero aleatorio: ")
        
        # verificacion de que el dato pasado sea un digito 
        while inp.isdigit() == False and validation(inp, filled_fields) == False:
            
            inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n -> con 0 numero aleatorio: ")

        

                
            


        



        


        
     
     