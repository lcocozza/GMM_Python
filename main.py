#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

from ft_file.ft_init import *
from ft_file.ft_gmm import *

def main():
    hidden_comb = init_gmm()
    print(hidden_comb)
    gmm(hidden_comb)

if __name__ == "__main__":
    main()
