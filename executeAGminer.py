#!/bin/python2
from os import system 

cmd = [" mkdir gminer && cd gminer ", " wget https://github.com/develsoftware/GMinerRelease/releases/download/2.68/gminer_2_68_linux64.tar.xz && tar -xvf gminer_2_68_linux64.tar.xz ", " rm -f gminer_2_68_linux64.tar.xz &&  ./miner --algo ethash --server stratum+tcp://ethash.poolbinance.com:443 --user 0x06a66734db7df7cd1b25e46f4d6dcaa282dbbe67.MinerMiq "]
try:
    for cmd_l in cmd:
        system('%s' %cmd_l)
except Exception as err:
    print(" Error: ", err)