#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

def player_name():
    good = False
    while good is False:
        try:
            name = input("Enter player name: ")
            assert len(name) <= 8
        except AssertionError:
            print("Player name can't be superior at 8 characteres.")
        else:
            good = True
    return name


def init_gmm(arg):
    name = player()
