##  AirBnB Clone -The Console

## Table of Contents
# 0x01 Introduction
# 0x02 Environment
# 0x03 Installation
# 0x04 Testing
# 0x05 Usage
# 0x06 Authors


## 0x01 Introductioni

Team project to build a clone of AirBnB.

This project is a command-line interpreter for managing AirBnB-like objects. It allows users to create, update, and delete objects such as User, Place, State, City, Amenity, and Review. The command interpreter supports both interactive and non-interactive modes, providing a convenient way to manage objects through commands.
The console is a command interpreter to manage objects abstraction between objects and how they are stored.



## Command Interpreter
The command interpreter is a key component of this project, enabling users to perform various actions and manage resources within the AirBnB system. The interpreter follows a simple command-driven interface where users can enter commands to perform operations like creating objects, updating attributes, and retrieving information.

## How to Start
To start the AirBnB command interpreter, follow these steps:

1.  Clone the repository to your local machine:
git clone https://github.com/your-username/AirBnB_clone.git

2. Navigate to the project directory:
cd AirBnB_clone

3. Run the command interpreter:
./console.py

How to Use
Once the command interpreter is running, you can use the following commands:

create: Create a new object instance.
show: Display information about a specific object.
destroy: Delete a specified object.
all: Display all objects or all objects of a specific type.
update: Update the attributes of a specified object.

For detailed information on available commands and their usage, you can use the help command within the interpreter.


The console will perform the following tasks:

create a new object
retrive an object from a file
do operations on objects
destroy an object

## Storage

All the classes are handled by the Storage engine in the FileStorage Class.
The purpose of this project is to understand how to:

## 0x02 Environment
Suite CRM terminal python Suite CRM Suite CRM git distributed version control system Github

Style guidelines:
* pycodestyle (version 2.7.*)
* PEP8
All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.

## 0x03 Installation

## HTML and CSS concepts
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

## Learning Objectives
* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS

## Requirements
# PYTHON SCRIPT REQUIREMENTS
* allowed editors: vi, vim, emacs
* the first line of all files should be exactly #!/usr/bin/python3
* all code should use the PEP8 style (version 1.7.*)
* all files must be executable
* all files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## PYTHON TEST CASE REQUIREMENTS
* all test files should be in the folder tests
* all test files should be text files (extension: .txt)
* all test files should be executed using the command python3 -m doctest ./tests/*
* all modules should have documentation python3 -c 'print(__import__("my_module").__doc__)'
* all functions (inside and outside of classes) should have documentation python3 -c 'print(__import__("my_module").my_funct\ ion.__doc__)'

## General
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be W3C compliant and validate with W3C-Validator
* All your CSS files should be in styles folder
* All your images should be in images folder
* You are not allowed to use !important and id (#... in the CSS file)
* You are not allowed to use tags img, embed and iframe
* You are not allowed to use Javascript
* Current screenshots have been done on Chrome 56 or more.
* No cross browsers
* You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

## Usage Examples for console
# Interactive Mode
~/me$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$

## Non-Interactive Mode
~/me$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

~/me$ cat test_help
help
~/me$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
~/me$

## Bugs
At this time, there are no known bugs.

## License
AirBnB Clone is open source and free to download and use

##Authors
Nnenna Njoku > nnennanjoku08@gmail.com
Ibraihim Fuhad Suma > ifuhad007@gmail.com
