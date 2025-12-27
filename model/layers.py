from random import choices
from math import exp

from base.support_functions import NormalizationFunctions, ActivationFunctions


class Attention(NormalizationFunctions):

    def __repr__(self) -> str:
        return f'Модуль: {__name__}; Класс: {self.__class__.__name__}; Адрес в памяти: {hex(id(self))}\n'


class Layers(ActivationFunctions):

    def __repr__(self) -> str:
        return f'Модуль: {__name__}; Класс: {self.__class__.__name__}; Адрес в памяти: {hex(id(self))}\n'
