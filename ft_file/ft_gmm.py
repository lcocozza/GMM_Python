from Global.data import *

def gmm():
    comb = ask_comb()


def ask_comb():
    good = False
    while good is False:
        try:
            comb = input("<> Enter combination : ")
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
    i = 0
    while i < len(liste):
        print(liste[i])
