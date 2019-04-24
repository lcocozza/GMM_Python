#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

from ft_file.ft_init import *
from ft_file.ft_gmm import *

def main():
    replay = True
    while replay is True:
        hidden_comb, pseudo = init_gmm()
        print(hidden_comb, pseudo)
        gmm(hidden_comb, pseudo)
        replay = replay_gmm()


if __name__ == "__main__":
    main()
