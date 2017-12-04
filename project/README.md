## i523 Final Project 
**Analysis of IoT / Big Data and Raspberry Pi IoT Monitor**

Packages needed outside of Python's standard library: 
* Kivy (https://kivy.org/docs/api-kivy.uix.label.html)
* Weather (https://pypi.python.org/pypi/weather-api)
* Beautiful Soup (https://pypi.python.org/pypi/beautifulsoup4)
* Requests (http://docs.python-requests.org/en/master/user/install/)

To compile Python project that creates Raspberry Pi IoT Monitor, please run `Makefile2` from the Linux prompt within the Raspberry Pi that contains the following commands for the proper dependencies: 
   
    #!/bin/sh
    all: packages program

    packages:
      sudo apt-get install python3-kivy
      sudo apt-get install python3-pip
      sudo apt-get install python-setuptools python-dev build-essential 
      sudo apt-get install python3-dev
      sudo apt-get install python-kivy python-kivy-examples debhelper python python-all-dev cython libgl1-mesa-dev libgles2-mesa-dev
      sudo apt-get docutils-doc python3-pygame python-pil-doc python3-pil-dbg ttf-bitstream-vera
      sudo easy_install pip
      sudo apt-get -f install
      pip install --upgrade pip
      pip3 install python3-weather-api
      sudo pip install requests
      pip3 install beautifulsoup4
      pip3 install Cython
      pip3 install h5py
      pip3 install kivy

    program: 
      python3 project.py

The final output should be in the form of the image below. If needed, the user can refresh their location in the input box to the left. 

![monitor](https://user-images.githubusercontent.com/31293179/33550867-6ee0d3b2-d8bd-11e7-8ad2-4a637fa3faef.png)
