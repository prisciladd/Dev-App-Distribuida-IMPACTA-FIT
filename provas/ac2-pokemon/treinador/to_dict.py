import jsons
from enum import Enum

def __enum_to_str(obj, **kwargs):
    return obj.__str__()

jsons.set_serializer(__enum_to_str, Enum)

def to_dict(obj):
    return jsons.dump(obj, strip_privates = True)

def to_dict_list(lista):
    resultado = []
    for item in lista:
        resultado.append(to_dict(item))
    return resultado