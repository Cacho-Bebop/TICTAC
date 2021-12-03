import os
from validation import inp_f
from winner import winner
#### the engine of the program.

def clear():
    
    os.system('clear')

def display_tictac_layout():
    
    row1 = [7,8,9]
    row2 = [4,5,6]
    row3 = [1,2,3]
    
    print(f"{row1}\n{row2}\n{row3}")

#display_tictac_layout()

def playing(p1_sim, p2_sim):
    
    """The game running"""
    keep_playing = True
        
    ### input of the players 

    counter   = 0 # contador de vueltas del loop
    
    p1_selections = [] 
    
    p2_selections = []
    
    turn = 1 # empezamos con el turno 1 
    
    # fields = [1,2,3,4,5,6,7,8,9] # structure index based 
    filled_fields = [] # lista de campos ya llenos
    
    who_win = 0 # variable que controla el jugador que ganò 0 empate | 1 p1 | 2 p2
    
    first_game  =   True # ? variable a utilizar para determinar si el juego recien comienza o no
    
    while keep_playing:
        
        print("\n\n")
        if first_game:
          
            fields = list(range(10))
            
            print(f"  {fields[7]}  |  {fields[8]}  |  {fields[9]}\n  {fields[4]}  |  {fields[5]}  |  {fields[6]}\n  {fields[1]}  |  {fields[2]}  |  {fields[3]}")
            
            first_game = False
        
        counter += 1
        # turn based input:
        if turn == 1 and who_win == 0 :
            
            x = (inp_f(turn, filled_fields)) #  ask user an input, puts in a not filled field
            
            p1_selections.append(int(x)) #  pone la seleccion de p1 en la lista de sus selecciones
            
            filled_fields.append(int(x)) #  coloca los numeros de los campos ya llenos
            
            fetch_field_and_fill(p1_selections, p2_selections, p1_sim, p2_sim,first_game) #  obtiene el campo y lo rellena
            
            turn = 2
            first_game = False
            
            # comprobamos si ya gano.
            if counter >= 3:
                if winner(p1_selections) == True:
                    
                        who_win = 1
                   
        elif turn == 2 and  who_win == 0:
                     
            y = (inp_f(turn, filled_fields))
            p2_selections.append(int(y))
            filled_fields.append(int(y))
            fetch_field_and_fill(p1_selections, p2_selections, p1_sim, p2_sim,first_game)
            
            # comprobamos si ya gano. 
            if counter >= 3:
                
                if winner(p2_selections) == True:
                    
                        who_win = 2
                        
            turn = 1
            
        if who_win == 1 or (who_win == 2):
            
            counter = 9
            show_winner(who_win)
            ask = 1
        
        elif who_win == 0 and (counter == 9):
            
            counter = 9
            print("Empate")
            ask = 1
            
        if (counter == 9) and ask:
            
            print("\n\nQuieres seguir jugando?[ Y: seguir jugando/ N or other character: terminar juego]\n")

            stay = input("> ")
            
            if(stay.casefold() == 'Y'.casefold()):

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
                    
def fetch_field_and_fill(fieldsp1, fieldsp2, simbolp1, simbolp2, first_play = True):

        clear()
        """Funcion encargada de rellenar el campo ingresadoss, y rellenar con el simbolo"""

        # si no es el primer juego entonces checkea los campos ya llenos
       
        x = ''
        fields = list( ' ' for x in range(10))
        
        for field in sorted(fieldsp1):
            
            fields[int(field)] = simbolp1
        
        for field in sorted(fieldsp2):
                
            fields[int(field)] = simbolp2
         
        # print(f"  {fields[7]}  |  {fields[8]}  |  {fields[9]}\n  {fields[4]}  |  {fields[5]}  |  {fields[6]}\n  {fields[1]}  |  {fields[2]}  |  {fields[3]}")
                    
        print(fields[7] + '|' + fields[8] + '|' + fields[9])
        print(fields[4] + '|' + fields[5] + '|' + fields[6])
        print(fields[1] + '|' + fields[2] + '|' + fields[3])                            
        #print(fields)

# def winner(selections):
    
    
#     """A partir del las selecciones, determinar si ganó"""
#     selections.sort()
    
#         # -> horizontal lines
#         # 1 2 3 - 4 5 6 - 7 8 9   
   
#     if (selections[0] == 1) and (selections[1] == 2) and (selections[2] == 3):
            
#             return True
    
#     elif (selections[0] == 4) and (selections[1] == 5) and (selections[2] == 6):
            
#             return True
    
#     elif (selections[0] == 7) and (selections[1] == 8) and (selections[2] == 9) :
#             return True
#     # -> vertical lines
#     # 1 4 7 - 2 5 8 - 3 6 9 
#     elif (selections[0] == 1) and (selections[1] == 4) and (selections[2] == 7):
            
#             return True

#     elif (selections[0] == 2) and (selections[1] == 5) and (selections[2] == 8):
            
#             return True
    
#     elif (selections[0] == 3) and (selections[1] == 6) and (selections[2] == 9):
#             return True
#     # -> diagonals 
#     # 1 5 9 - 3 5 7
   
#     elif ((selections[0] == 1) and (selections[1] == 5) and (selections[2] == 9)) or ((selections[0] == 3) and (selections[1] == 5) and (selections[2] == 7)):
        
#         return True
    
#     else:
        
#         return False    

def show_winner(winner):
    
    print(f"The winner is -> player {winner}.\nCONGRATULATIONS!!!")