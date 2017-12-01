#!/usr/bin/python3
all: packages program

packages:
	sudo apt-get install python3-pip
	sudo apt-get install python3-kivy
	sudo apt-get install python-setuptools python-dev build-essential 
	sudo easy_install pip
	pip3 install python3-weather-api
	sudo pip install requests
	apt-get install python3-bs4

program: 
	python3 project.py
