def combi_player(nb_play = 4):
    pass
    #tab_test = [["A",2],["B",3],["C",4]]
    
    #tab_user=[0,0] for i in range(nb_play)]
    valide = False
    combi = ''

    while valide==False:
        combi.append(input('Veuillez rentrer une combinaison de couleurs et de formes: '))
        if len(combi) != 2*nb_play :
            valide = False

        for i in range(len(combi)):
            for j in range(nb_play):
                if i != None:
                
                    tab_user[j][0] = combi[i]
                else :
                    print("Erreur, veuillez remplir toutes les cases.")
                    valide = False
                    i = len(combi)
        valide = True
        
    return tab_user




def good_format(string, nb):
    liste = list(string)
    
    if len(string) != ((nb * 3) - 1):
        return False
    
