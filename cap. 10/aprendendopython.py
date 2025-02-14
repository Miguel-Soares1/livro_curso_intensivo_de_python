from pathlib import Path
path = Path('aprendendopython.txt')
contents = path.read_text()
print(contents)
lines = contents.splitlines()
c_string = ''
for line in lines:
    c_string += line.lstrip()
print(c_string)