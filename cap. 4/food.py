my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods [:]

my_foods.append('apple pie')
friend_foods.append('strogonoff')

print('my favorite foods are:')
for food in my_foods:   
    print(food)

print('my friends favorite foods are:')
for friendfood in friend_foods:
    print(friendfood)