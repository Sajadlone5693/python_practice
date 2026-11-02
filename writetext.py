from pathlib import Path
import os

pat=Path('spam.txt')
pat.write_text('hello,world')

pat.read_text()


# print(int(pat.stat().st_size)/1024)
# print(Path.cwd())

# os.chdir(r'/Users/shahnaz/Desktop/python/python1')
# print(pat.is_absolute())
# pats=str(Path('spam', 'bacon', 'eggs'))
# print(pats)
# my_files = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in my_files:
# 	print(Path(r"/Users/shahnaz/Desktop/python", filename)