# -------------------Task1-------------------

import os
from pprint import pprint

BASE_PATH = os.getcwd()
LOGS_NAME = 'logs'
FILE_NAME = 'recipes.txt'

full_path = os.path.join(BASE_PATH, LOGS_NAME, FILE_NAME)

def cook_book_func(full_path):
  cook_book = {}
  with open(full_path) as file_obj:
    foot = file_obj.readline().strip()
    for line in file_obj:
      quantyti = int(line.strip())
      lines = []
      for items in range(quantyti):
        data = file_obj.readline().strip().split(' | ')
        lines.append({'ingredient_name': data[0], 'quantity': data[1], 'measure': data[2]})        
      cook_book[foot] = lines 
      file_obj.readline()
      foot = file_obj.readline().strip()  
  return cook_book

# pprint(cook_book_func(full_path), sort_dicts=False)

# ----------------------Task2-------------------
    
def get_shop_list_by_dishes(dishes, person_count, full_path):
  result = {}  
  cook_book = cook_book_func(full_path)
  menu = list(cook_book.keys())
  for dish in dishes:
    if dish not in menu:
      print(f'Блюдо: {dish} - нет в меню!')    
    order = cook_book[dish]
    for ingredient in order:    
      ing_name = ingredient['ingredient_name']
      if ingredient['ingredient_name'] not in result:      
        ing_quan = int(ingredient['quantity']) * int(person_count)
        ing_maen = ingredient['measure'] 
        result[ing_name] = {'measure': ing_maen, 'quantity': ing_quan}   
      else:     
        result[ing_name]['quantity'] += int(ingredient['quantity']) * int(person_count)     
  return result

pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2, full_path))

# ----------------------Task3-------------------

base_path = os.getcwd()
log_path = 'files'
catalog_path = os.path.join(base_path, log_path)

list_files = os.listdir(catalog_path)

def merging(puth):
  list_files = os.listdir(puth)
  dict_file = {}
  
  for file in list_files: 
    puth_file = os.path.join(catalog_path, file)
    
    with open(puth_file) as name_file:
      quan_str = len(name_file.readlines())      
      name_file.seek(0)      
      data_file = name_file.read()
      
      dict_file[quan_str] = {'name': file, 'data': data_file}   
      sorted_file_tuple = sorted(dict_file.items(), key=lambda x: x[0])
      sorted_file_dict = dict(sorted_file_tuple) 

  with open('mergin.txt', 'w') as file_merging:
    for key, value in sorted_file_dict.items():
      result = str(key) + '\n' + value['name'] + '\n' + value['data']
      file_merging.write(result + '\n')    

merging(catalog_path)



