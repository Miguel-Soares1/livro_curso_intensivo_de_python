from pathlib import Path
import json

path = Path('numerofavorito.json')
numero = int(input('digite seu numero favorito: '))
contents = json.dumps(numero)
path.write_text(contents)