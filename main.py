import sys
import os
import re
from colorama import init, Fore

init(autoreset=True)

class ProductList:
    def __init__(self):
        self.options = sys.argv[1:]
        self.file_name = self.options[0]
        self.action = self.options[1]

    def add_to_list(self):
        if not os.path.exists(f'{self.file_name}.txt'):
            open(f'{self.file_name}.txt', 'w').close()
        file = open(f'{self.file_name}.txt', 'r')
        product_list = file.readlines()
        product_list = set(product_list)

        print(f'{Fore.YELLOW}Название: ', end='')
        name = input()
        print(f'{Fore.YELLOW}Цена: ', end='')
        price = input()

        if name and price:
            product_list.add(f'{name} - {price}\n')
            f = open(f'{self.file_name}.txt', 'w')
            for product in product_list:
                f.writelines(product)
            print(f'\n{Fore.GREEN}{name} успешно добавлен!')
        else:
            print(f'{Fore.RED}[-] Вы не указали название или цену!')

    def change_list(self):
        file = open(f'{self.file_name}.txt', 'r')
        product_list = file.readlines()
        i = 0
        for product in product_list:
            i += 1
            product = product.replace('\n', '')
            print(f'{Fore.GREEN}{i}) {product}')

        print(f'\n{Fore.YELLOW}Введите номер строки которую хотите именить: ', end='')
        num = input()
        print(f'\n{Fore.YELLOW}Название: ', end='')
        name = input()
        print(f'{Fore.YELLOW}Цена: ', end='')
        price = input()

        if num and name and price:
            num = int(num)
            product_list[num-1] = f'{name} - {price}\n'
            print(f'\n{Fore.GREEN}Изменения успешно внесены в список!')
            f = open(f'{self.file_name}.txt', 'w')
            f.writelines(product_list)

        else:
            print(f'{Fore.RED}[-] Вы не указали название, цену или номер строки!')

    def remove_from_list(self):
        file = open(f'{self.file_name}.txt', 'r')
        product_list = file.readlines()
        i = 0
        for product in product_list:
            i += 1
            product = product.replace('\n', '')
            print(f'{Fore.GREEN}{i}) {product}')

        print(f'\n{Fore.YELLOW}Введите номер строки которую хотите удалить: ', end='')
        num = input()

        if num:
            num = int(num)
            product_list.pop(num - 1)
            f = open(f'{self.file_name}.txt', 'w')
            f.writelines(product_list)
            print(f'\n{Fore.RED}Элемент успешно удалён!')

    def total_amount(self):
        file = open(f'{self.file_name}.txt', 'r')
        product_list = file.readlines()
        product_list = ''.join(product_list)
        prices = re.split('\D+', product_list)
        while '' in set(prices):
            prices.remove('')

        int_prices = []
        for price in prices:
            int_prices.append(int(price))

        total_prices = sum(int_prices)
        print(f'\n{Fore.GREEN}Общая сумма: {total_prices} сомони')

    def list(self):
        print(f'\n{Fore.GREEN}Список!\n')
        file = open(f'{self.file_name}.txt', 'r')
        product_list = file.readlines()
        i = 0
        for product in product_list:
            i += 1
            product = product.replace('\n', '')
            print(f'{Fore.GREEN}{i}) {product}')

if __name__ == '__main__':
    my_product_list = ProductList()
    if my_product_list.action == 'add':
        my_product_list.add_to_list()

    elif my_product_list.action == 'change':
        my_product_list.change_list()

    elif my_product_list.action == 'remove':
        my_product_list.remove_from_list()

    elif my_product_list.action == 'amound':
        my_product_list.total_amount()

    elif my_product_list.action == 'list':
        my_product_list.list()