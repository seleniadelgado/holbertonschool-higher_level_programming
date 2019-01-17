ReadMe for Input/Output project

Task 0.
Function that reads a text file (UTF8) and prints it to stdout.
Must use with statement
Did no import any module.

Task 1.
Function that returns the number of lines of a text file:
Did not import any module.

Task 2.
Function that reads n lines of a text file and prints it to stdout.
Use with statement
Did not import any module.

Task 3.
Function that writes a string to a text file (UTF8) and returns the number of
characters written.
Did not import any module.
Should override the content of the file if it already exists.

Task 4.
Function that appends a string at the end of a text file (UTF8) and returns the
number of characters added.
Did not import any module.

Task 5.
Function that returns the JSON representation of an object (string).

Task 6.
Function that returns an object (Python data structure) represented by a
JSON string:

Task 7.
Function that writes an Object to a text file, using a JSON representation
Did not need to manage exceptions if the object can’t be serialized.
Did not need to manage file permission exceptions.

Task 8.
Function that creates an Object from a “JSON file”
Use with statement.

Task 9.
Script that adds all arguments to a Python list, and then saves them to a file.
Uses function load_from_json_file from 8-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
Did not need to manage file permissions / exceptions.

Task 10.
Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of an
object.
obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary, string,
integer and boolean
You are not allowed to import any module

Task 11.
Class Student that defines a student by:

Public instance attributes:
first_name
last_name
age

Task 12.
Make a class Student that defines a student by: (based on 11-student.py)

Public instance attributes:
first_name
last_name
age

Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None):
that retrieves a dictionary representation of a Student instance
(same as 10-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must
be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

Task 13.
Make a class Student that defines a student based on Task 12.

Task 14.
Technical interview prep.
function that returns a list of integer representing the Pascal's triangle of n.
Returns an empty list if n <= 0.
n will always be an integer.