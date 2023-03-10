#0x00. AirBnB clone - The console

#0x00.Table of contents
#0x01 Introduction
#0x02 Environment
#0x03 Installation
#0x04 Testing
#0x05 Usage
#0x06 Authors

#Introduction
A project built by me to build a clone of AirBnB.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the Wiki.

The console will perform the following tasks:

create a new object
retrive an object from a file
do operations on objects
destroy an object

#Usage
To launch the console application in interactive mode simply run:

console.py 

or to use the non-interactive mode run:

echo "your-command-goes-here" | ./console.py 

#Commands
Commands	Description	Usage
help or ?	Displays the documented commands.	help
quit	Exits the program.	quit
EOF	Ends the program. Used when files are passed into the program.	N/A
create	Creates a new instance of the <class_name>. Creates a Json file with the object representation. and prints the id of created object.	create <class_name>
show	Prints the string representation of an instance based on the class name and id.	show <class_name class_id>
destroy	Deletes and instance base on the class name and id.	destroy <class_name class_id>
all	Prints all string representation of all instances based or not on the class name	all or all <class_name class_id>
update	Updates an instance based on the class name and id by adding or updating attribute	update <class_name class_id key value>
Tests
If you wish to run at the test for this application all of the test are located under the test/ folder and can execute all of them by simply running:

python3 -m unittest discover tests 

from the root directory.
