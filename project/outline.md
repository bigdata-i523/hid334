#

## Introduction
### High level discussion of IoT/Big Data
* Recent growth / projections
* How they're related
* Relevance to my project

## Project
### Description
* Brief overview of language/packages used
* Why this project is a synthesis of output from other Big Data problems to create an IoT device
	* Google News: 
		* Description as a Big Data problem 
			* Size / Importance / Algorithms used to solve the problem
	* Weather Underground
		* Description as an IoT / Big Data example
			* How IoT / Big Data has improved analysis over traditional methods
### Data Used
* RSS Feeds for News / Scores using XML
	* XML vs. YAML
* MQTT in IoT for use in the Raspberry Pi
	* What is MQTT? 
	* Advantages / Disadvantages over traditional data retrieval
	
### Results
* Refresh rate: secondly
* Bytes used (build): 966656
* Bytes used (refresh): 1032	
	```python
	from pympler import asizeof
	obj = WeatherWidget()
	print(asizeof.asized(obj, detail=1).format())
	```	
## Developing Areas in IoT 
### Edge Computing 
* Description
* Current Use Cases
### Security
* Vulnerabilities in current technology
* Solutions being discovered
### Voice Recognition
* New dimension of user data
* User behavior with IoT 
