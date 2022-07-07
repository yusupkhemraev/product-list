import os
import sys
import json
import argparse
from art import *
from colorama import init, Fore

init(autoreset=True)


class ProductList:
    def __init__(self):
        tprint('Product List')
        parser = argparse.ArgumentParser()

        parser.add_argument('-f', '--file-name', dest='file_name', help='Название файла', required=True)
        parser.add_argument('-a', '--action', dest='action',
                            help='Пожалуйста, укажите действие.'
                                 'add - Добавить, change - Изменить,'
                                 'remove - Удалить, amount - Итоговая сумма',
                            required=True)
        self.args = parser.parse_args()

        if not self.args.file_name:
            parser.error('[-] Пожалуйста укажите название файла без расширения, используйте --help для получения '
                         'дополнительной информации.')
        elif not self.args.action:
            parser.error('[-] Пожалуйста укажите действие, используйте --help для получения дополнительной информации.')

        if self.args.action == 'append':
            self.append_to_list()
        elif self.args.action == 'change':
            self.change_list()
        elif self.args.action == 'remove':
            self.remove_from_list()
        elif self.args.action == 'sum':
            self.total_price()
        else:
            parser.error('[-] Действие не найдено, используйте --help для получения дополнительной информации.')

    def append_to_list(self):
        product_list = []
        if not os.path.exists(f'{self.args.file_name}.json'):
            open(f'{self.args.file_name}.json', 'w', encoding='utf-8').close()

        with open(f'{self.args.file_name}.json', 'r', encoding='utf-8') as f:
            try:
                product_list = json.load(f)
                if not product_list:
                    print(f'{Fore.MAGENTA}[-] Список пуст!')
            except json.decoder.JSONDecodeError:
                pass

        print(f'\n{Fore.YELLOW}[*] Название: ', end='')
        name = input()
        if not name:
            print(f'{Fore.RED}[-] Вы не ввели название. Повторите ввод')
            sys.exit()

        try:
            print(f'\n{Fore.YELLOW}[*] Цена: ', end='')
            price = float(input())
            product_list.append({'name': name, 'price': price})
            print(f'\n{Fore.GREEN}[+] {name} успешно добавлен!')

            with open(f'{self.args.file_name}.json', 'w', encoding='utf-8') as file:
                json.dump(product_list, file, indent=4, ensure_ascii=False)

        except ValueError:
            print(f'{Fore.RED}[-] Вы ввели не число. Повторите ввод')

    def change_list(self):
        if not os.path.exists(f'{self.args.file_name}.json'):
            open(f'{self.args.file_name}.json', 'w', encoding='utf-8').close()

        with open(f'{self.args.file_name}.json', 'r', encoding='utf-8') as f:
            try:
                product_list = json.load(f)
                if product_list:
                    for i, product in enumerate(product_list, start=1):
                        print(f'{Fore.YELLOW}{i}. {product["name"]} - {product["price"]}')
                else:
                    print(f'{Fore.MAGENTA}[-] Список пуст!')
                    sys.exit()

            except json.decoder.JSONDecodeError:
                return print(f'{Fore.MAGENTA}[-] Список пуст!')

        print(f'\n{Fore.YELLOW}[*] Что хотитие изменить?: ', end='')
        old_name = input()
        if not old_name:
            print(f'{Fore.RED}[-] Вы не ввели название. Повторите ввод')
            sys.exit()

        print(f'\n{Fore.YELLOW}[*] Новое название: ', end='')
        name = input()
        if not name:
            print(f'{Fore.RED}[-] Вы не ввели новое название. Повторите ввод')
            sys.exit()

        try:
            print(f'\n{Fore.YELLOW}[*] Новая цена: ', end='')
            price = float(input())

            for product in product_list:
                if old_name == product['name']:
                    product['name'] = name
                    product['price'] = price
                    print(f'\n{Fore.GREEN}[+] {old_name} успешно изменён на {name}')

            with open(f'{self.args.file_name}.json', 'w', encoding='utf-8') as f:
                json.dump(product_list, f, indent=4, ensure_ascii=False)

        except ValueError:
            print(f'{Fore.RED}[-] Вы ввели не число. Повторите ввод')

    def remove_from_list(self):
        if not os.path.exists(f'{self.args.file_name}.json'):
            open(f'{self.args.file_name}.json', 'w', encoding='utf-8').close()

        with open(f'{self.args.file_name}.json', 'r', encoding='utf-8') as f:
            try:
                product_list = json.load(f)
                if product_list:
                    for i, product in enumerate(product_list, start=1):
                        print(f'{Fore.YELLOW}{i}. {product["name"]} - {product["price"]}')
                else:
                    print(f'{Fore.MAGENTA}[-] Список пуст!')
                    sys.exit()

            except json.decoder.JSONDecodeError:
                return print(f'{Fore.MAGENTA}[-] Список пуст!')

        print(f'\n{Fore.YELLOW}[*] Что хотитие удалить?: ', end='')
        name = input()
        if not name:
            print(f'{Fore.RED}[-] Вы не ввели название. Повторите ввод')
            sys.exit()

        for product in product_list:
            if name == product['name']:
                product_list.remove({'name': name, 'price': product['price']})
                print(f'\n{Fore.RED}[+] {name} успешно удалён')

        with open(f'{self.args.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(product_list, f, indent=4, ensure_ascii=False)

    def total_price(self):

        if not os.path.exists(f'{self.args.file_name}.json'):
            open(f'{self.args.file_name}.json', 'w', encoding='utf-8').close()
        with open(f'{self.args.file_name}.json', 'r', encoding='utf-8') as f:
            try:
                product_list = json.load(f)
                if not product_list:
                    print(f'{Fore.MAGENTA}[-] Список пуст!')
                    sys.exit()

            except json.decoder.JSONDecodeError:
                return print(f'{Fore.MAGENTA}[-] Список пуст!')

        total = []
        for product in product_list:
            total.append(product["price"])

        print(f'{Fore.GREEN}[+] Итоговая цена: {sum(total)}')


if __name__ == '__main__':
    p = ProductList()
