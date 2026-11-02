import re
from pathlib import Path

user_input=input("enter a regex to search:")
pattern=re.compile(user_input)


for file in Path.cwd().glob('*.txt'):
	with open(file) as f:
		for line in f:
			if pattern.search(line):
				print(f'file: {file.name}\nmatches regex: {user_input} \nline: {line}')