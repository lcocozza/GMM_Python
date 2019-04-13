from random import randint as ri

#Renvoie un caractère dans un tableau
def search_in_tab(tab, string) :
    for i in range(len(tab)) :
        if string == tab[i] : return i

    return -1


def random_combination(colors,shapes,nb_play) :
    tab_combi = [[0,0] for i in range(nb_play)]

    for i in range(nb_play) :
        tab_combi[i][0] = ri(0,len(colors)-1)
        tab_combi[i][1] = ri(0,len(shapes)-1)

    return tab_combi

def search_color_shape_place(tab_user,tab_combi,nb_play):
    count =0
    for i in range (nb_play):
        if tab_user[i][0]==tab_combi[i][0] and tab_user[i][1]==tab_combi[i][1] : count+= 1
    return count



def search_color_place(tab_user,tab_combi,nb_play):
    count=0
    for i in range (nb_play):
        if tab_user[i][0]==tab_combi[i][0] :count+=1
    return count




def search_shape_place(tab_user,tab_combi,nb_play):
    count=0
    for i in range (nb_play):
        if tab_user[i][1]==tab_combi[i][1] :

            count+=1
    return count



def search_color_shape(tab_user,tab_combi,nb_play):
    count=0
    tab_combi_modif = [[tab_combi[i][0],tab_combi[i][1]] for i in range(len(tab_combi))]
    for i in range (nb_play):
        for n in range (nb_play):
            if tab_user[i][0]==tab_combi_modif[n][0] and tab_user[i][1]==tab_combi_modif[n][1] :
                count+=1
                tab_combi_modif[n][0] = -1

    return count


def test(tab_combi, enter,):
    


def return_combination (colors = ['red','blue','yellow'],shapes=['&','?','$'],nb_play = 4):
    tab_user=[[0,0]for i in range(nb_play)]
    color, shape ='',''
    
    for i in range (nb_play):
        color = input('Entrez la couleur : ')
        shape = input('Entrez la forme : ')
        tab_user[i][0] = search_in_tab(colors,color)
        tab_user[i][1] = search_in_tab(shapes,shape)

    return tab_user



        
        


def main ():
    colors=[]
    shapes=[]
    nb_play =0
    tab_combi = []
    



    
    nb_play=int(input('Rentrez le nombre de case: '))
    for i in range(int(input('Entrez le nombre de couleur de jeu: '))) :
        colors.append(input('Entrez la couleur : '))
    for i in range(int(input('Entrez le nombre de forme de jeu: '))) :
        shapes.append(input('Entrez la forme : '))

    tab_combi=random_combination(colors,shapes,nb_play)

    #print(tab_combi)
    
    
    

if __name__ == '__main__' :
    main()
