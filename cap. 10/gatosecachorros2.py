from pathlib import Path
try:
    with open ('dog.txt') as d:
        contents = d.read()
    with open ('cat.txt') as c:
        contents2 = c.read()
except FileNotFoundError:
    pass
else:
    print(contents + '\n' + contents2)