Description:

The AirBnB Command Interpreter is a command-line tool developed for the AirBnB project. It provides an interactive shell for managing instances of different classes.

How to start the command interpreter:

1. Clone the AirBnB_clone project repository
2. Be in the AirBnB_clone repository
3. Run console.py with: ./console.py

How to use the command interpreter:

- quit: Exits command interpreter
- EOF: Exits command interpreter using end-of-file (EOF)
- create: Create new instance of the specified class
- show: Display the string representation of an instance
- destroy: Delete an instance
- all: Display all instances or instances of a specific class
- update: Update an instance by adding or modifying an attribute

Examples:

- Exits command interpreter:

	quit

- Exits command interpreter with EOF:

	EOF

- Create new instance of BaseModel:

	create BaseModel

- Show the string representation of an instance:

	show BaseModel 1234-1234

- Deletes an instance:

	delete BaseModel 1234-1234

- Displays all instances or a certain instance:

	all
	all BaseModel

- Updates an instance:

	update BaseModel 1234-1234 name "New Name"
