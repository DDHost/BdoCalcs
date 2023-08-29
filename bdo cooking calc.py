import math

chiken = {
    "chiken": 2,
    "deep oil": 6,
    "wine": 2,
    "slat": 1,
}

beer = {
    'Grains': 5,
    'Mineral Water': 6,
    'Leavening Agent': 2,
    'Sugar': 1,
}


dishes = [chiken,beer]

def calcDish(main,dish):
    print('\n')
    print('\n')
    ingredientsName = list(dish.keys())
    ingredients = list(dish.values())

    main = math.floor(main/ingredients[0])
    for i in range(0,len(ingredients)):
        print(f'{ingredientsName[i]}:{ingredients[i]*main}')
    
    print(f'\n In total: {main} \n')

   

def main():
    while True:
        print('''
        1. Chicken
        2. Beer

        0. To exit
        ''')
        option = int(input('Please enter the dish number: ')) - 1
        if(option == -1):
            print('bye!')
            break
        main = int(input(f'Please enter the amount of {list(dishes[option])[0]} you have: '))
        calcDish(main,dishes[option])
        option = input('Continue[y/n] \n')
        if(option == 'n'):
            print('bye!')
            break

main()

