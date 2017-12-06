#!/usr/bin/env python
all: packages program

packages:
	sudo apt-get -f install
	sudo apt-get install python3-pip
	sudo pip3 install python3-weather-api
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get upgrade
	sudo apt-get install python3-kivy
	
program: 
	python3 project.py
