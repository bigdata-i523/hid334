#!/bin/sh
all: packages program

packages:
	sudo apt-get -f install
	sudo apt-get install python3-pip
	pip3 install --upgrade python3-pip
	pip3 install python3-weather-api
	sudo pip install requests
	pip3 install beautifulsoup4
	pip3 install Cython
	pip3 install h5py
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get upgrade
	sudo apt-get install python3-kivy
	sudo apt-get install build-essential zlib1g-dev libssl-dev libffi-dev python3-dev
	sudo apt-get python3-pygame python-pil-doc python3-pil-dbg ttf-bitstream-vera
	
program: 
	python3 project.py
