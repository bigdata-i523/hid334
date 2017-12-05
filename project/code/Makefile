#!/bin/sh
all: packages program

packages:
	sudo apt-get install pip
	pip install --upgrade pip
	pip install weather-api
	sudo pip install requests
	pip install beautifulsoup4
	pip install Cython
	pip install h5py
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get update
	sudo apt-get install python-kivy
	
program: 
	python project.py
