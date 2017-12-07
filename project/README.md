# i523 Final Project 
Peter Russell
## Topic 
The goal of this project was to explore the relationship between IoT and Big Data through one of the most popular and accessible IoT devices, the Raspberry Pi 3. This project builds an application for the Raspberry Pi that allows the user to see current weather, forecasts, local news, a quote of the day, top business/political news and sports scores. The user has the ability to update if they desire to do so and all links to news stories are clickable to the websites themselves.

## Notes

* For best results, the application should be maximized for best spacing. 
* Please be patient during the `makefile` build. 
  * Kivy is the most time intensive. In our tests, we have found from a blank machine, it could take up to 10 minutes to build. 
* As the application is loaded, there will be a 5 second delay of the screen being black as the images are built. Once you see 'DailyView' at the top toolbar, you know the application was built. 
* Changing the location will cause the app to update after 3-4 seconds and once a website is clicked, a similar amount of time will take to load the browser.

## Required Packages
This application should require minimal user intervention to get up and running. In the `code` folder (https://github.com/bigdata-i523/hid334/tree/master/project/code), there is a `Makefile` that the user can run from the command line to install the necessary dependencies. The setup assumes a minimally set up Raspberry Pi to execute the program. However, the user should have `sudo` installed to run the make file. If this has not yet been done, please follow the few steps here (https://www.privateinternetaccess.com/forum/discussion/18063/debian-8-1-0-jessie-sudo-fix-not-installed-by-default) to install `sudo` before running the `Makefile`. 

### References for Required Packages
Packages needed outside of Python's standard library: 
* Kivy (https://kivy.org/docs/api-kivy.uix.label.html)
* Weather (https://pypi.python.org/pypi/weather-api)
* Beautiful Soup (https://pypi.python.org/pypi/beautifulsoup4)
* Requests (http://docs.python-requests.org/en/master/user/install/)
## Testing
This application was tested using a Virtual Machine with Debian since this is the operating system that Raspbian is based off of (Raspberry Pi's operating system). 
![debian_output](https://user-images.githubusercontent.com/31293179/33682599-08d705f2-da96-11e7-8886-754a36cd2e9d.PNG)

## Final Output
The final result should look like the following based off the user's own location: 
![output](https://user-images.githubusercontent.com/31293179/33682700-51d3829e-da96-11e7-86b0-f3306b0ed311.PNG)

