#!/bin/sh
all: packages program

packages:
	sudo apt-get install python3-kivy
	sudo apt-get install python-setuptools python-dev build-essential 
	sudo easy_install pip
	sudo pip install weather-api
	sudo pip install requests
	sudo pip install bs4

program: 
	python3 project.py
