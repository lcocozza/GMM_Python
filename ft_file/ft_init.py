from Global.data import *
from random import randrange as rr

def init_gmm():
    pseudo = player_pseudo()
    print("""===========================================================
    GRAND MASTER MIND : play the Grand Master Mind game
  Note : enter an empty line to stop the interaction loop
===========================================================""")
    get_settings()
    return gen_comb(), pseudo


def player_pseudo():
    good = False
    while good is False:
        try:
            pseudo = input("<> Enter player pseudo : ")
            pseudo = pseudo.strip()
            if pseudo == "":
                pseudo = "Anonymous"
            assert len(pseudo) <= 9
        except AssertionError:
            print("The pseudo can't be superior at 9 characteres.")
        else:
            good = True
    return pseudo


def get_settings():
    good = False
    while good is False:
        try:
            config = input("<> Enter game configuration : ")
            config = config.strip()
            assert set_settings(config) == True
        except AssertionError:
            print("Tu t'es nique Robert.")
        else:
            good = True


def set_settings(config):
    global settings
    if config == "":
        return True
    config = config.split()
    for i in range(len(config)):
        param = config[i].split('=')
        if len(param) == 2:
            if param[0] in settings:
                if param[0] == "size":
                    if param[1].isdigit() is True:
                        settings["size"] = int(param[1])
                    else:
                        return False
                else:
                    size = settings["size"]
                    settings[param[0]] = param[1][:size].upper()
    return True


def gen_comb():
    global settings
    i = 0
    hidden_comb = []
    size = settings["size"]
    while i < size:
        hidden_comb.append(settings["letters"][rr(len(settings["letters"]))])
        hidden_comb.append(settings["digits"][rr(len(settings["digits"]))])
        if i < (size - 1):
            hidden_comb.append(' ')
        i += 1
    return "".join(hidden_comb)


def replay_gmm():
    good = False
    while good is False:
        try:
            retry = input("do you want retry ? [y/n]: ").lower()
            assert retry == 'y' or retry == 'n'
        except AssertionError:
            print("please enter 'y' or 'n'")
        else:
            good = True
    return True if retry == 'y' else False
