from pathlib import Path
path = Path('aprendendopython.txt')
contents = path.read_text()
lines = contents.splitlines()
c_string = ''
for line in lines:
    c_string += line.lstrip()
txt = c_string.replace('python', 'C') 
print(txt)