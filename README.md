# AIRBnB CLONE
----
<p align="center"><img src="bnb.png" alt="AirBnb  logo"></p>

## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## The Console                                                                                                   
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

   -Create a new object (ex: a new User or a new Place)  
   -Retrieve an object from a file, a database etc…  
   -Do operations on objects (count, compute stats, etc…)  
   -Update attributes of an object  
   -Destroy an object  
   
## Commands and Functions
The command interpreter allows us to handle our data requirements with the following commands:
                                                                                                                      
| Command | Function |                                                                                                
| ------- | ------------------------------------ |
| create | create a new instance of a class |
| show | show the info of an instance of a class |
| destroy | destroy an instance of a class |
| update | update the info of the objects in an instance |
| all | update the info of the objects in an instance |
| quit | exit the console |
| help | show the help commands |

## Objects
These are the objects that you can pass to the command console

| Object | Function |                                                                                                
| ------- | -------- |
| city | City of the reservation |
| state | Country state of the reservation |
| place | Name of the place of reservation |
| user | Name of the user who makes reservation |
| amenity | Benefits of the place |
| review | Reviews of the place |

### Using the console
start the console with
```./console```
you will see:
```(hbnb)```
and start to use the hbnb console
## How to use the HBNB console
### Syntax:
``` <command> <classname> <id>```
id does not apply to create command
### For help:
```help <command>```
### Examples:
#### For Help:
```
(hbnb)help create
Create a new instance of a class
(hbnb)
```
#### For standard commands:
```
(hbnb)create User
993e570d-9b4e-449c-84b3-085ab454d3ce
(hbnb)
```
It will create a new User
``` 
(hbnb)create BaseModel
d711be23-73d9-4fbd-92f5-fe9ec7044d6d
(hbnb)show BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
[BaseModel] (d711be23-73d9-4fbd-92f5-fe9ec7044d6d) {'id': 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d', 'created_at': '2019-07-04T02:20:53.149558', 'updated_at': '2019-07-04T02:20:53.149791'}
(hbnb)
 ```
 It will create a new BaseModel and show the objects of the instance
 
```
(hbnb)destroy BaseModel d711be23-73d9-4fbd-92f5-fe9ec7044d6d
['BaseModel', 'd711be23-73d9-4fbd-92f5-fe9ec7044d6d']
(hbnb)
```
## Authors
Shavin Lillkant <Shavz>
