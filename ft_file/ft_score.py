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


def player_score(add=0):
    global pseudo
    if check_file("scores.ini") == False:
        score = {pseudo: 0 + add}
    else:
        fd_file = open("scores.ini", "rb")
        file_unpick = Unpickler(fd_file)
        score = file_unpick.load()
        fd_file.close()
        if pseudo in score:
            score[pseudo] += add
        else:
            score[pseudo] = add
    fd_file = open("scores.ini", "wb")
    file_pick = Pickler(fd_file)
    file_pick.dump(score)
    fd_file.close()
    return score[pseudo]
