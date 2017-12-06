# i523 Final Project 
Peter Russell
## Topic 
The goal of this project was to explore the relationship between IoT and Big Data through one of the most popular and accessible IoT devices, the Raspberry Pi 3. This project builds an application for the Raspberry Pi that allows the user to see current weather, forecasts, local news, a quote of the day, top business/political news and sports scores. The user has the ability to update if they desire to do so. 

## Required Packages
This application should require minimal user intervention to get up and running. In the `code` folder (https://github.com/bigdata-i523/hid334/tree/master/project/code), there is a `Makefile` that the user can run from the command line to install the necessary dependencies. The setup assumes a minimally set up Raspberry Pi to execute the program. However, the user should have `sudo` installed to run the make file. If this has not yet been done, please follow the few steps here (https://www.privateinternetaccess.com/forum/discussion/18063/debian-8-1-0-jessie-sudo-fix-not-installed-by-default) to install `sudo` before running the `Makefile`. 

**Please try to be patient in running the `Makefile` as several dependencies need to be installed for the GUI package, Kivy, to run properly.**

### References for Required Packages:
Packages needed outside of Python's standard library: 
* Kivy (https://kivy.org/docs/api-kivy.uix.label.html)
* Weather (https://pypi.python.org/pypi/weather-api)
* Beautiful Soup (https://pypi.python.org/pypi/beautifulsoup4)
* Requests (http://docs.python-requests.org/en/master/user/install/)

## Final Output: 
The final result should look like the following based off the user's own location: 

![monitor](https://user-images.githubusercontent.com/31293179/33550867-6ee0d3b2-d8bd-11e7-8ad2-4a637fa3faef.png)
