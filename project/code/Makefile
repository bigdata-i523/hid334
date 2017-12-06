#!/usr/bin/env python
all: packages program

packages:
	sudo apt-get -f install
	sudo apt-get install python3-pip
	sudo apt-get install -y \
    	python-pip \
    	build-essential \
    	git \
    	python \
    	python-dev \
    	ffmpeg \
    	libsdl2-dev \
    	libsdl2-image-dev \
    	libsdl2-mixer-dev \
    	libsdl2-ttf-dev \
    	libportmidi-dev \
    	libswscale-dev \
    	libavformat-dev \
    	libavcodec-dev \
    	zlib1g-dev
	sudo pip3 install python3-weather-api
	sudo add-apt-repository ppa:kivy-team/kivy
	sudo apt-get upgrade
	sudo apt-get install python3-kivy

program: 
	python project.py
