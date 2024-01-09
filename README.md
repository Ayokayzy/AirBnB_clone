# AirBnB Clone - The Console						09.01.24

                                        AUTHORS
1. Kayzy Gboluwaga                      ALX Software Engineering Student
2. Samuel Ayitey                        ALX Software Engineering Student

## Overview

This project is the first step in building a full-fledged AirBnB clone web application. It focuses on creating a command-line interface (CLI) that allows users to manage objects (such as Users, Places, and Reviews) that will eventually be part of the website.

## Objectives

BaseModel Class:
Define a foundation for all model classes, including:
id: Unique identifier (UUID)
created_at: Timestamp of object creation
updated_at: Timestamp of last object update
save(): Persist object data to storage
to_dict(): Convert object to a dictionary
Command Line Interpreter:
Implement commands for:
create: Create new objects
show: Display specific objects by ID
destroy: Delete objects
all: List all objects of a given type or all types
update: Modify existing objects
quit or EOF: Exit the console
help: Display command usage instructions
## Installation

Clone the repository:
Bash
git clone https://github.com/<your-username>/AirBnB_clone.git
Use code with caution. Learn more
Navigate to the project directory:
Bash
cd AirBnB_clone
Use code with caution. Learn more
## Usage

Run the console:
Bash
./console.py
Use code with caution. Learn more
Enter commands within the console:
(hbnb) help  # Display available commands
(hbnb) create BaseModel  # Create a new BaseModel instance
(hbnb) show BaseModel 1234-abcd  # Show details of a specific BaseModel
# ... and so on
## Testing

Run the test suite to ensure functionality:

Bash
python test_console.py
Use code with caution. Learn more
## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for discussion.
