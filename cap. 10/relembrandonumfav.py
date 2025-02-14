from pathlib import Path
import json

path = Path('numerofavorito.json')

def getnumfav(path):
    if path.exists():
        contents = path.read_text()
        if contents.strip():
            numero = json.loads(contents)
            return numero
    else:
        return None
    
def relembrandonumfav():
    numero = getnumfav(path)
    if numero:
        print(f'Eu sei o seu número favorito! É {numero}')
    else:
        numero = int(input('Digite seu número favorito: '))
        contents = json.dumps(numero)
        path.write_text(contents)

relembrandonumfav()
