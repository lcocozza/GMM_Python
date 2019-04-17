from Global.data import *

def init_gmm():
    player_pseudo()
    print("""===========================================================
    GRAND MASTER MIND : play the Grand Master Mind game
  Note : enter an empty line to stop the interaction loop
===========================================================""")
    get_settings()


def player_pseudo():
    global pseudo
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


def get_settings():
    global settings
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
    config = config.split(' ')
    for i in config:
        param = config[i].split('=')
