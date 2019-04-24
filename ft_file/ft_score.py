from Global.data import *
from pickle import *
from operator import itemgetter

def check_file(filename):
    exist = True
    try:
        fd_file = open(filename, "r")
    except FileNotFoundError:
        fd_file = open(filename, "w")
        exist = False
    finally:
        fd_file.close()
    return exist


def player_score(pseudo, pts):
    """..."""
    global settings
    config = str(settings["size"]) + str(len(settings["letters"])) + str(len(settings["digits"]))
    if check_file("scores.ini") == False:
        liste = [(pseudo, pts)]
        score = {config: liste}
    else:
        fd_file = open("scores.ini", "rb")
        file_unpick = Unpickler(fd_file)
        score = file_unpick.load()
        fd_file.close()
        if config in score.keys():
            liste = score[config]
            liste = sort_list(liste, pseudo, pts)
        else:
            liste = [(pseudo, pts)]
        score[config] = liste
    fd_file = open("scores.ini", "wb")
    file_pick = Pickler(fd_file)
    file_pick.dump(score)
    fd_file.close()
    return score


def sort_list(liste, pseudo, pts):
    """..."""
    liste.append((pseudo, pts))
    sorted(liste, key=itemgetter(1), reverse=True)
    if len(liste) > 10:
        liste.pop()
    return liste


def print_score(score):
    for elemment in score:
        print("Score for configuration type: size={}.".format(elemment[0]))
        for pseudo, pts in score[elemment]:
            print("\t{}: {} turn.".format(pseudo, pts))
