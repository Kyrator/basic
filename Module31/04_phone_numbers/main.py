# TODO здесь писать код
import re

nambers = ['9999999999', '999999-999', '99999x9999']


def chek(nambers_check):
    """ Функция проверки номера телефона"""
    names_list = ['первый номер:', 'второй номер:', 'третий номер:', 'четвертый номер:', 'пятый номер:']
    count = -1
    for i in nambers_check:
        count += 1
        res = re.findall(r'[8-9]\d{9}', i)
        if len(res) == 1:
            print(names_list[count], 'всё в порядке')
        else:
            print(names_list[count], 'не подходи')


chek(nambers)
