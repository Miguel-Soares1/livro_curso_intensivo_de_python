from pathlib import Path
import json

path = Path('numerofavorito.json')
contents = path.read_text()
numeros = json.loads(contents)
print(f'Eu sei o seu numero favorito! É {numeros}')