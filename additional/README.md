## Lecture Length Script ##

### Summary ### 
This script scrapes the times of the videos from the Theory section of the class website. It should be dynamic enough to adjust for changes to the number of sections or modules within those sections. 

### Packages Needed ###
* requests, urllib3, bs4, pandas, lxml, re

### Future Improvements ###
* Adjusting minor typos on the website to reduce special case handling for more concise code (ie. Health Informatics section 3.4.1.2 - 3.4.1.7) (lines 58-59) 
* The renaming of multiple videos under a module from 'Video 1:' to 'Video I:'. This would help differentiate modules whose times begin as 'Video 1:xx:xx' from a successor video (Video I) with the goal being more compact code. (lines 69-71)
* Section sorting in final output - Python currently reads 3.1 > 3.10 > 3.2

### Reference website ###
Class website: https://cloudmesh.github.io/classes/i523/2017

### Times as of 2017-09-30 ###

| Section 	|            Section Title            	| Total Time 	|
|:-------:	|:-----------------------------------:	|:----------:	|
|   3.1.  	|             Introduction            	|   6:24:09  	|
|   3.2.  	|       Overview of Data Science      	|   2:29:46  	|
|   3.3.  	|      Big Data Use Cases Survey      	|   5:20:50  	|
|   3.4.  	|    Health Informatics Case Study    	|   2:21:43  	|
|   3.5.  	| e-Commerce and LifeStyle Case Study 	|   2:22:51  	|
|   3.6.  	|          Physics Case Study         	|   3:07:17  	|
|   3.7.  	|           Radar Case Study          	|   0:21:56  	|
|   3.8.  	|          Sensors Case Study         	|   2:04:58  	|
|   3.9.  	|          Sports Case Study          	|   3:23:06  	|
|  3.10.  	|      Web Search and Text Mining     	|   1:39:25  	|
