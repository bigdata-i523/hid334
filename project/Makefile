#!/usr/bin/python3
all: program

packages:
	pip3 install kivy
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get install python3-kivy
	sudo apt-get update
	sudo apt-get install python3-pip
	sudo apt-get install python-setuptools python-dev build-essential 
	sudo apt-get install python3-dev
	sudo apt-get docutils-doc python3-pygame python-pil-doc python3-pil-dbg ttf-bitstream-vera
	sudo easy_install pip
	sudo apt-get -f install
	pip install --upgrade pip
	pip3 install python3-weather-api
	sudo pip install requests
	pip3 install beautifulsoup4
	pip3 install Cython
	pip3 install h5py

program: 
	python3 project.py
