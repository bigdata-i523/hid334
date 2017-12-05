#!/bin/sh
all: packages program

packages:
	pip3 install python3-weather-api
	sudo pip install requests
	pip3 install beautifulsoup4
	pip3 install Cython
	pip3 install h5py
	sudo apt-get install python3-kivy-common
	sudo apt-get install python3-kivy-bin
	sudo apt-get install build-essential zlib1g-dev libssl-dev libffi-dev python3-dev
	sudo apt-get docutils-doc python3-pygame python-pil-doc python3-pil-dbg ttf-bitstream-vera
	sudo apt-get install python3-pip
	pip install --upgrade python3-pip
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get -f install python3-kivy

program: 
	python3 project.py
