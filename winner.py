lista = [1,4,5,3,7]

def winner(camp):
    
    camp = set(camp)
    # horizontal
    comb_1 = {1,2,3}
    comb_2 = {4,5,6}
    comb_3 = {7,8,9}
    #vertical
    comb_4 = {1,4,7}
    comb_5 = {2,5,8}
    comb_6 = {3,6,9}
    #diagonal
    comb_7 = {7,5,3}
    comb_8 = {1,5,9}
    

    if   (camp.intersection(comb_1) == comb_1):
        return True
    elif (camp.intersection(comb_2) == comb_2):
        return True
    elif (camp.intersection(comb_3) == comb_3):
        return True
    elif (camp.intersection(comb_4) == comb_4): 
        return True
    elif (camp.intersection(comb_5) == comb_5):
        return True
    elif (camp.intersection(comb_6) == comb_6):
        return True
    elif (camp.intersection(comb_7) == comb_7):
        return True
    elif (camp.intersection(comb_8) == comb_8):
        return True
    else:
        False


print(winner(lista))