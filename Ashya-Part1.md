# Ashya Collector

This part of the project is to make a service that takes pictures and sends the pictures to a list of URLs

## Part 1

The requirements are the following: 

1. [x] Should be written in latest version of Python 3.x
1. [x] Program can be called something like ```ashya-collector.py```
1. [x] Starts up as a running service that runs on port 5050.  
1. [x] Service may be a [flask](http://flask.pocoo.org/docs/0.12/python3/) application so that it can be queried from time to time. If not flask, some other WSGI.
1. [x] Checks the ```~/urls.json``` file for which URLs to send data too. (See below for the format).  The URLs are kept in a global class variable that is in memory throughout the duration of the program.  The program checks this file every 1 minute to see if there are changes and then modifies the 
1. [x] Running the command: ```curl localhost:5050/urls``` should return the current URLs that the application is servicing. 
1. [ ] Create two docker images that will dockerize the application.  The first docker image runs on x86 and the second runs on Raspberry Pi. If you only need one docker image then that is fine too.  The Docker image should be called ```ashya/collector``` 



### ```~/urls.json``` format

The file will look as follows: 

```json

{ "urls" : 
	[ 
		"https://ashya.ai/stream/sana", 
  		"https://foobar.com/uploads/joud",
    ]
}
```
This is just a standard JSON file.  The file will be changed overtime by another program that will monitor smart contracts to see which URLs have been allowed to monitor. 

## Part 2

Add the following to the ```ashya-collector.py``` service.  Have it run in a loop every 1 minute or as fast as possible that does the following:

1. [ ] Use the [pycamera](http://picamera.readthedocs.io/en/release-1.13/) or some other library to take a picture.  It may be that OpenCV is used directly with just one of the libraries below. 
1. [ ] Process the image using darknet, keras, or some other object detection to determine what objects are in the image. 
1. [ ] Create a JSON data out of the output of the darknet/YOLO process.  Format it as shown below. 
1. [ ] Take the json and make a ```POST``` request to send to all of the URLs that you captured in part 1 from the ```~/urls.json``` file. 
1. [ ] Running the command ```curl localhost:5050/objects``` should return the json information shown below or the last message sent to the other urls. 


### JSON body to be sent to POST request format

Formatted example might look like the following:

```json
{
	"timestamp": "2017-10-08T00:19:30.000",
	"objects": [
		{"object" : "basketball" , "certainty" : ".77"},
		{"object" : "chair", "certainty" : ".40"},
		{"object" : "table", "certainty" : ".20"}
	]
}
```
