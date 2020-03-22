# JsonNestedDictParser

TECHNICAL CHALLENGE SOLUTION 
(Colen Liu)

_________________________________________________________________________________________________________________

OVERVIEW:

Given a JSON file that encodes a nested key-value structure, my solution, named getKeysAndOccurrences, 
stores each key present in the structure as well as the number of occurrences for each of those keys. The newly 
created mapping is converted to JSON, and then printed to STDOUT.

The getKeysAndOccurrences function makes use of two helper functions: the get_all_keys function from the 
nested_lookup package and a custom-made getAllOccurrences function. The get_all_keys function fetches all keys 
from a dictionary, and returns a list of the keys. The getAllOccurrences obtains the number of occurrences of 
each element found in a given list, and returns a dictionary of all elements in the list and a count of their
respective number of occurrences.

_________________________________________________________________________________________________________________

REQUIREMENTS:

- Python 3.8+
- Works on Linux, Windows, macOS

_________________________________________________________________________________________________________________

INSTALL:

- install from pypi using pip:
	=> pip install nested-lookup

- OR easy_install:
	=> easy_install nested-lookup

- OR install from source using:
	=> git clone https://github.com/russellballestrini/nested-lookup.git
	=> cd nested-lookup
	=> pip install .

_________________________________________________________________________________________________________________

HOW TO RUN:

1. Make sure to follow one of the INSTALL instructions above to install the nested-lookup package.
	=> if using IntelliJ, go to Tools -> Manage Python Packages... -> + (on right side) -> 
		search up "nested-lookup" -> Install Package

2. Replace the 'ENTER PATH TO DESIRED JSON FILE HERE' on line 9 with the path to the JSON file that will be parsed.
	=> e.g. mine looked like this after: with open('c:/Users/liuco/Downloads/source-data3.json')...

3. Build and run!





