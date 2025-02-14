#sequencia if elif else pra determinar qual fase da vida a pessoa esta
age = int(input('quantos anos voce tem? '))
if age < 2:
    print('voce ainda é um nenem')
elif age >= 2 and age < 4:
    print('voce ja é uma criança')
elif age >= 4 and age < 13:
    print('voce ja é um(a) garoto(a)')
elif age >= 13 and age < 20:
    print('voce ja é um(a) adolescente')
elif age >= 20 and age < 65:
    print('voce ja é um(a) adulto(a)')  
else:
    print('voce ja e um(a) idoso(a)')