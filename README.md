# The AirBnB Clone Project

___

![Image link](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2015/06/airbnb_logo_detail.png)

## Description of the project
___

This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

## Description of the command interpreter:
___
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming

Some of the commands available are:

- show
- creat
- update
- destroy
- count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:

- Creating new objects (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Doing operations on objects (count, compute stats, etc…)

## How to start it
___
These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

## installing
___
You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

user git clone we cloned the resparatory.
## Repo Contents
___

This repository constains the following files:

|File| Description|
|:-------|:-------|
|Authors| Contains info about authors of the project|
|base_model.py| Defines BaseModel class (parent class), and methods|
|file_storage.py|Creates new instance of class, serializes and deserializes data|
|console.py|  creates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object|

and allof the sub clases and unittest files in the directory.

# Console
___
The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

# Storage
___
The above classes are handled by the abstracted storage engine defined in the FileStorage class.

Every time the backend is initialized, AirBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

# How to use it
____
It can work in two different modes:

_Interactive and Non-interactive._

In Interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In Non-interactive mode, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.

```python
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

# Format of Command Input
___

In order to give commands to the console, these will need to be piped through an echo in case of Non-interactive mode.

In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.

# Available commands and what they do
___

The recognizable commands by the interpreter are the following:

|Command| Description|
|:------|:-----------|
|create| Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file 'file.json'.|
|Usage| create class name|
|show| Prints the string representation of a class instance based on a given id|
|destroy| Deletes a class instance based on a given id. The storage file file.json is updated accordingly.
|all| Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.|
|count| Retrieves the number of instances of a given class.|
|update| Updates an instance based on the class name and id by adding or updating attribute (saves the changes into a JSON file).|
# Authors
___
Noah Tsegay|  [https://github.com/Noaht8]

Yirga Beyene|  [https://github.com/proyirga]
