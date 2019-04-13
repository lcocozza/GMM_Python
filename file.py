#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

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

def player_score(name, add=0):
    if check_file("scores.ini") == False:
        score = {name: 0 + add}
    else:
        fd_file = open("scores.ini", "rb")
        file_unpick = Unpickler(fd_file)
        score = file_unpick.load()
        fd_file.close()
        if name in score:
            score[name] += add
        else:
            score[name] = add
    fd_file = open("scores.ini", "wb")
    file_pick = Pickler(fd_file)
    file_pick.dump(score)
    fd_file.close()
    return score[name]
