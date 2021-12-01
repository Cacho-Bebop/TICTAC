from random import randint, seed

def display_tictac_layout():
    
    row1 = [7,8,9]
    row2 = [4,5,6]
    row3 = [1,2,3]
    
    print(f"{row1}\n{row2}\n{row3}")

#display_tictac_layout()

def playing2(p1_sim, p2_sim):
    
    q = ''
    fields = ['','','','','','','','','','','']
    
    layout = f"  {fields[7]}  |  {fields[8]}  |  {fields[9]}\n  {fields[4]}  |  {fields[5]}  |  {fields[6]}\n  {fields[1]}  |  {fields[2]}  |  {fields[3]}"
    

    """The game running"""
    keep_playing = True
        
    ### input of the players 
    inp_p1 = 0
    
    inp_p2 = 0
    
    counter_1 = 0
    counter_2 = 0
    ### guardamos las selecciones de los jugadores
    p1_selections = [] 
    
    p2_selections = []
    
    turn = 1
    
    # fields = [1,2,3,4,5,6,7,8,9] # structure index based 
    filled_fields = []
    
    who_win = 0
    
    first_game  =   True
    while keep_playing:
        
        # turn based input:
        if turn == 1 and who_win == 0:
            
            print("\nTurno de jugador 1")
            counter_1 += 1
            x = (recibir_campo(turn, filled_fields))
            p1_selections.append(int(x))
            filled_fields.append(int(x))
            fields[int(x)+1] = p1_sim
            display_layout(layout)
            turn = 2
            first_game = False
            
            if counter_2 == 3:
                
                if winner(p1_selections) == True:
                    
                    who_win = 1
                   
        elif turn == 2 and who_win == 0:
            
            print("\nTurno de jugador 2")
            counter_2 += 1
            y = (recibir_campo(turn, filled_fields))
            p2_selections.append(int(y))
            filled_fields.append(int(y))
            fields[int(y)+1] = p2_sim
            display_layout(layout)
            turn = 1
            
            if counter_2 == 3:
                
                if winner(p2_selections) == True:
                    
                    who_win = 2
            
          
            
            
        if (counter_1 == 3 and counter_2 == 3) and who_win == 0:
            
            print("\nEmpate\nQuieres seguir jugando?[ Y: seguir jugando/ N or other character: terminar juego]\n")

            stay = input("> ")
            
            if(stay == 'Y'):
                
                inp_p1 = 0
    
                inp_p2 = 0
    
                counter_1 = 0
                counter_2 = 0
                
                ### guardamos las selecciones de los jugadores
                p1_selections = [] 
    
                p2_selections = []
    
                turn = 1
    
                # fields = [1,2,3,4,5,6,7,8,9] # structure index based 
                filled_fields = []
    
                who_win = 0
    
                first_game  =   True
            
            else:
            
                keep_playing = False
        
        elif who_win == 1 or who_win == 2:
            
            show_winner(who_win)
            
def validation(field, filled_fields):

        """Validacion de que el campo seleccionado no pertenezca a los campos ya llenos"""

        if field in filled_fields:
            
            return False
        
        else:
            
            return True
                     
def recibir_campo(turn, filled_fields):
    
    """funcion encargada de manejar el turno / recibir entrada / corroborar que sea valida"""
        
    # mostramos de quien es el turno
    print(f"Is turn of the player {turn}")
    
    while True:
        
        # muestra informacion necesaria
        inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n->")
        
        # verificacion de que el dato pasado sea un digito 
        while (inp.isdigit() == False or validation(inp, filled_fields) == False):
            
            inp = input("\nIndica con numeros del 1 al 9 en cual campo deseas marcar\n-> ")


            seed(101)
            # si es 0 a inp le asignamos un numero random
            if inp == 0:

                while validation(inp, filled_fields) == False:
                    
                        inp = randint(1,9)
                            
        # Una vez verificada la validez de la seleccion, devolverla
        return  inp


def display_layout(layout):
    
    print(layout)
                    
        #print(fields)

def winner(selections):
    """A partir del las selecciones, determinar si ganó"""
    selections.sort()
    
    if selections[0] == 1 or selections[0] == 4 or selections[0] == 7:
        
        if (selections[1] == selections[0] + 1) and (selections[2] == selections[1] + 1):
            
            return True
        
    elif selections[1] == selections[0] + 3:
        
        if ( selections[2] == selections[1] + 3 ):    
            
            return True
    
    elif (selections[0] == 1 and selections[1] == 5 and selections[2] == 9) or (selections[0] == 3 and selections[1] == 5 and selections[2] == 7):
        
        return True
    
    else:
        
        return False    


def show_winner(winner):
    
    print(f"The winner is -> player {winner}.\nCONGRATULATIONS!!!")