from math import exp


class SupportFunctions:
    __slots__ = ('unwanted_characters', 'punctuation_characters')

    def __init__(self):
        self.unwanted_characters: str = r'`[]~@#$%^&*_\+=}(){$"«»<>\|\\№•‘’“”\t\n±×÷§©®™°µ¶'
        self.punctuation_characters: str = '!?.,;:—-'

    @staticmethod
    def format_string(token: float | str, length: int = 7) -> str:
        string = f'{{:.{length}f}}'
        return string.format(token)

    @staticmethod
    def calculate_average(value: list[float] | tuple[float]) -> float:
        return sum(value) / len(value)


class DerivativeFunctions(SupportFunctions):

    @staticmethod
    def get_elu_derivative(x: list[float], i: int, alpha=1.0) -> float:
        return 1 if x[i] > 0 else alpha * exp(x[i])

    @staticmethod
    def get_tanh_derivative(tanh, x: float) -> float:
        return 1 - tanh(x) ** 2


class ActivationFunctions(SupportFunctions):

    @staticmethod
    def get_elu(x: float, alpha: float = 1.0) -> float:
        return x if x >= 0 else alpha * (exp(x) - 1)

    @staticmethod
    def get_tanh(x: float) -> float:
        exp_pos_2x: float = 1.0
        exp_neg_2x: float = 1.0

        for i in range(1, 11):
            exp_pos_2x *= (2 * x) / i + 1
            exp_neg_2x *= (2 * -x) / i + 1

        return (exp_pos_2x - exp_neg_2x) / (exp_pos_2x + exp_neg_2x)


class NormalizationFunctions(SupportFunctions):

    @staticmethod
    def get_softmax(x: list[float]) -> list[float]:
        exp_values: list[float] = [exp(i - max(x)) for i in x]
        sum_exp: float = sum(exp_values)
        return [i / sum_exp for i in exp_values]


class InitializationFunctions:

    @staticmethod
    def get_uniform(value: float = 0.5) -> tuple[float, float]:
        return -value, value

    @staticmethod
    def get_xavier(input_size: int, output_size: int) -> tuple[float, float]:
        limit: float = (6 / (input_size + output_size)) ** 0.5
        return -limit, limit

    @staticmethod
    def get_he(input_size: int) -> tuple[float, float]:
        limit: float = (2 / input_size) ** 0.5
        return -limit, limit
