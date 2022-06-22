import sys
import os
import re
from colorama import init, Fore

init(autoreset=True)

options = sys.argv[1:]
file_name = options[0]
action = options[1]

product_list = []

def add_to_list():
    if not os.path.exists(f'{file_name}.txt'):
        open(f'{file_name}.txt', 'w').close()
    file = open(f'{file_name}.txt', 'r')
    product_list = file.readlines()
    product_list = set(product_list)

    print(f'{Fore.YELLOW}Название: ', end='')
    name = input()
    print(f'{Fore.YELLOW}Цена: ', end='')
    price = input()

    if name and price:
        product_list.add(f'{name} - {price}\n')
        f = open(f'{file_name}.txt', 'w')
        for product in product_list:
            f.writelines(product)
        print(f'\n{Fore.GREEN}{name} успешно добавлен!')
    else:
        print(f'{Fore.RED}[-] Вы не указали название или цену!')