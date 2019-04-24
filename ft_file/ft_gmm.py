from Global.data import *
from ft_file.ft_score import *
from sys import exit

def gmm(hidden_comb, pseudo):
    turn = 0
    comb = ""
    liste = []
    while comb != hidden_comb:
        comb = ask_comb()
        result = test_comb(comb, hidden_comb)
        liste.append("{}: {}".format(comb, result))
        print_list(liste)
        turn += 1
    print("!!! COMBINATION FOUND IN {} TURNS !!!".format(turn))
    score = player_score(pseudo, turn)
    print_score(score)


def ask_comb():
    good = False
    while good is False:
        try:
            comb = input("<> Enter combination : ")
            comb = comb.strip()
            if comb == "":
                exit()
            comb = comb.upper()
            assert good_format(comb) == True
        except AssertionError:
            print("Tu t'es nique Roger.")
        else:
            good = True
    return comb


def good_format(string):
    global settings
    liste = list(string)
    i = 0
    if len(string) != ((settings["size"] * 3) - 1):
        return False
    while i <= ((settings["size"] * 3) - 3):
            if string[i].isalpha() is False:
                return False
            i += 3
    i = 1
    while i <= ((settings["size"] * 3) - 2):
        if string[i].isdigit() is False:
            return False
        i += 3
    return True


def print_list(liste):
    for i in range(len(liste)):
        print(liste[i])


def test_comb(comb, hidden_comb):
    result = ""
    comb = comb.split()
    hidden_comb = hidden_comb.split()
    count = search_color_shape_place(comb, hidden_comb)
    result += "A={}, ".format(count)
    count = search_color_shape(comb, hidden_comb)
    result += "B={}, ".format(count)
    count = search_color_place(comb, hidden_comb)
    result += "C={}, ".format(count)
    count = search_shape_place(comb, hidden_comb)
    result += "D={}.".format(count)
    return result


def search_color_shape_place(tab_user, tab_combi):
    global settings
    count = 0
    for i in range(settings["size"]):
        if tab_user[i][0] == tab_combi[i][0] and tab_user[i][1] == tab_combi[i][1]:
            count += 1
    return count


def search_color_place(tab_user, tab_combi):
    global settings
    count = 0
    for i in range(settings["size"]):
        if tab_user[i][0] == tab_combi[i][0]:
            count += 1
    return count


def search_shape_place(tab_user, tab_combi):
    global settings
    count = 0
    for i in range(settings["size"]):
        if tab_user[i][1] == tab_combi[i][1]:
            count += 1
    return count


def search_color_shape(tab_user, tab_combi):
    global settings
    count = 0
    tab_combi_modif = [[tab_combi[i][0], tab_combi[i][1]] for i in range(len(tab_combi))]
    for i in range(settings["size"]):
        for n in range(settings["size"]):
            if tab_user[i][0] == tab_combi_modif[n][0] and tab_user[i][1] == tab_combi_modif[n][1]:
                count += 1
                tab_combi_modif[n][0] = -1
    return count
