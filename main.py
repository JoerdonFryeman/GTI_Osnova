import re
from random import uniform, choice

from base.base import get_json_data, logger
from base.support_functions import InitializationFunctions, SupportFunctions
from text_processor.dictionary_creator import DictionaryCreator
from model.train_many_to_many import ManyToMany
from model.train_many_to_one import ManyToOne
from model.generator import TextGenerator
from model.data import DataPreparation, Classification
from model.neural_network import Builder

init_func = InitializationFunctions()
support = SupportFunctions()
dictionary_creator = DictionaryCreator()
train_mtm = ManyToMany()
train_mto = ManyToOne()
bd = Builder()
gen = TextGenerator()
cl = Classification()

if __name__ == '__main__':
    dev = 'В разработке...'
    logger.info(dev)
    print(f'\n{dev}')
