from dadata import Dadata
from work_with_sqlite import token, url, language


dadata = Dadata(token)

def desired_location(word):
    result = dadata.suggest(url, word, language=language)
    return result


def address_coordinates(address):
    result = dadata.suggest(url, address, language=language, count=1)
    return('широта ' + str(result['data']['geo_lat']) + ' долгота ' + str(result['data']['geo_lon']))


def gui():
    print('-----------------------------------------------------------')
    print('Добро пожаловать!')
    while True:
        print('-----------------------------------------------------------')
        print('Введите какое примерно место хотите найти\nЕсли хотите закрыть ПО напишите "Закрыть"')
        print('-----------------------------------------------------------')
        location = input()
        if location == 'Закрыть':
            print('-----------------------------------------------------------')
            print("До новых встреч!")
            print('-----------------------------------------------------------')
            break
        result = desired_location(location)
        for i in range(len(result)):
            print(result[i]['value'])
        print('-----------------------------------------------------------')
        print("Введите адресс, чтобы узнать координаты")
        print('-----------------------------------------------------------')
        address = input()
        print(address_coordinates(address))


if __name__ == "__main__":
    gui()
