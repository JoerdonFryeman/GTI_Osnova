from base.base import save_json_data, logger
from base.support_functions import ActivationFunctions, DerivativeFunctions
from .neural_network import Builder


class ManyToOne(Builder, DerivativeFunctions, ActivationFunctions):
    pass
