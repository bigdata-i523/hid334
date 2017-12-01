#!/usr/bin/python3
all: packages program

packages:
	sudo apt-get install python3-pip
	sudo apt-get install python3-kivy
	sudo apt-get install python-setuptools python-dev build-essential 
	sudo easy_install pip
	pip3 install python3-weather-api
	sudo pip install requests
	pip3 install beautifulsoup4
	pip3 install kivy

program: 
	python3 project.py
