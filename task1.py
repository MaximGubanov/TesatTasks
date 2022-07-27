""" 1. Implement a function with two arguments, both are lists of possibly different length. The function must return
    a dictionary (dict for Python or object for JS) with keys from the first list and corresponding values from the
    second. If a key lacks value, the resulting dictionary must contain None for that key (or null for JavaScript).
    Redundant values must be ignored. Keys are guaranteed to be unique.
"""
import json

# ключей больше, чем значений (ключи дублируются)
l1 = ['a', 'b', 'c', 'd', 'd', 'd', 'e', 'f', 'f', 'g']
l2 = [1, 2, 3, 4, 5]

# значений большеб чем ключей
l3 = ['a', 'b', 'c']
l4 = [1, 2, 3, 4, 5, 6]


def gen_dict(key_list, value_list, json_format=True):
    """ json_format, если True, то вернёт json-объект, поумодчанию возвращает dict
    """
    dct = {}

    key_list = remove_duplicates(key_list)

    for value_index, key in enumerate(key_list):
        try:
            dct.update({key: value_list[value_index]})
        except IndexError:
            dct.update({key: None})

    return json.dumps(dct) if json_format else dct


def remove_duplicates(lst):
    """Исключение дубликатов-ключей в списке
    """
    new_lst = []
    for x in lst:
        if x not in new_lst:
            new_lst.append(x)
    return new_lst


d = gen_dict(l1, l2)
print(d)
