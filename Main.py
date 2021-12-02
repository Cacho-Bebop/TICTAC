from motor import playing
####TIC-TAC-TOE GAME####

# players:

#display first menu:
def display_welcome():
    
    """first menu / just a welcome """
    
    print("Hi! Welcome to the TIC-TAC-TOE game!\nremember:\n-> at least we gonna need two players, thank you!!")
    
     
def select_playerONE():

    """Player one selects a simbol"""
    # now player 1 selects between X or O
    
    choice = ''
     
    while True:
        
        print("\nPlayer 1 -> select [X or O]:\n")
        choice = input("-> ")
        
        if choice == 'X' or choice == 'O':
            break
        

    return choice 

def determination(p1_choice):
    
    """Check the player 1 selection, return the other disponible simbol to player 2"""
    
    if p1_choice == 'X':
    
        return 'O'
    
    else:
        
        return 'X'


def print_selected_simbols():
    
    """Displays the simbols selected by the players"""
    print(f"Remember!\n\nP1 -> {P1_choice}\nP2 -> {P2_choice}\n\n\nLet's play!")
    

### variables to store players choice
P1_choice  =   ''
P2_choice  =   ''

### welcome menu
display_welcome()
# -> p1 selecciona su simbolo
P1_choice = select_playerONE()
# -> p2 recibe el simbolo disponible (el contrario que se reciba por P1)
P2_choice = determination(P1_choice)
# -> se muestran los resultados
print_selected_simbols()
playing(P1_choice, P2_choice)
    
    