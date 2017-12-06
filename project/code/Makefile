#!/usr/bin/env python
all: packages program

packages:
	sudo apt-get -f install
	sudo apt-get install python3-pip
	sudo apt-get install cython3 python3-dev
	sudo apt-get install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev
	pip3 install git+https://github.com/kivy/kivy.git@master
	sudo apt-get install -y \
    	python-pip \
    	build-essential \
    	git \
    	python \
    	python-dev \
    	ffmpeg \
    	libportmidi-dev \
    	libswscale-dev \
    	libavformat-dev \
    	libavcodec-dev \
    	zlib1g-dev
	sudo pip3 install python3-weather-api
	sudo pip3 install bs4
	sudo pip3 install requests
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get upgrade
	sudo apt-get install python-kivy
	
program: 
	python3 project.py
