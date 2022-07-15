from pprint import pprint
import os
# задание 1

with open('recipes.txt', encoding='utf-8') as file_obj:
    cook_book = {}
    for line in file_obj:
        cook_book[line.strip()] = []
        quantity = int(file_obj.readline())
        ingredients_list = []
        for item in range(quantity):
            ingredients = {}
            data = file_obj.readline().strip().split('|')
            ingredients['ingredient_name'] = data[0]
            ingredients['quantity'] = data[1]
            ingredients['measure'] = data[2]
            ingredients_list.append(ingredients)
        cook_book[line.strip()] = ingredients_list
        file_obj.readline()

    pprint(cook_book)


# задание 2
def get_shop_list_by_dishes(dishes, person_count): # dishes - [], person_count - int
    order = {}
    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                if item['ingredient_name'] not in order:
                    order[item['ingredient_name']] = {'measure': item['measure'], 'quantity': int(item['quantity']) * person_count}
                else:
                    order[item['ingredient_name']]['quantity'] += int(item['quantity']) * person_count
        else:
            print(f'Блюдо {dish} не представлено в меню')
    return pprint(order)

get_shop_list_by_dishes(['Утка по-пекински', "Утка по-пекински", 'Омлет', 'Суп'], 2 )


# Задание 3
files_dir = os.path.join(os.getcwd(), 'NetologyFiles')
files_list = os.listdir(files_dir)

# os.getcwd() - текущая рабочая директория
# os.listdir(path=".") - список файлов и директорий в папке
# os.path.join(path1[, path2[, ...]]) - соединяет пути

def files_sorting(files_list):
    sorting_list = []
    for file in files_list:
        with open(os.path.join(files_dir, file), encoding='utf-8') as file_obj:
            sorting_list.append((file, len(file_obj.readlines())))
    sorting_list.sort(key=lambda x: x[1])
    # print(sorting_list)
    with open('result.txt', 'w', encoding='utf-8') as new_file:
        for file_name, lines in sorting_list:
            new_file.write(file_name + '\n' + str(lines) + '\n')
            with open(os.path.join(files_dir, file_name), encoding='utf-8') as initial_file:
                for row in initial_file:
                    new_file.write(row.strip() + '\n')

# files_sorting(files_list)