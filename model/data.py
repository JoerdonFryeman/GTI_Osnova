from base.base import get_json_data, save_json_data, logger
from base.support_functions import SupportFunctions
from text_processor.encoder import TextEncoder


class DataPreparation:
    """Класс предназначен для работы с массивами данных."""

    __slots__ = ('data_name', 'serial_class_number', 'serial_data_number', 'dataset')

    def __init__(self):
        """
        Инициализирует объекты класса с параметрами по умолчанию.

        :param data_name (str): Ключ-название массива данных.
        :param serial_class_number (int): Начальный порядковый номер класса данных.
        :param serial_data_number (int): Начальный порядковый номер данных.
        :param dataset (dict): Загружаемый массив данных.
        """
        self.data_name: str = 'classes'
        self.serial_class_number: int = 1
        self.serial_data_number: int = 1
        self.dataset: dict = get_json_data('memory/mto_weights', 'input_dataset')

    def get_data_dict_value(self, value_type: str) -> int:
        """
        В зависимости от флага возвращает количество данных или имя "класса" данных.

        :param value_type: Флаг "типа" данных.
        :return: Количество данных или имя "класса" данных.
        """
        if value_type == 'serial_data_number':
            return len(dict(enumerate(self.dataset[self.data_name].get(str(self.serial_class_number), [])[0], 1)))
        elif value_type == 'serial_class_number':
            return len(dict(enumerate(self.dataset[self.data_name])).keys())
        else:
            raise ValueError(f'Неизвестный тип значений: {value_type}')

    def get_data_dict(self, serial_class_number: int) -> dict:
        """
        Возвращает словарь данных.

        :param serial_class_number: Порядковый номер класса данных.
        :return: Словарь с данными, где ключи - порядковые номера классов изображений.
        """
        return dict(enumerate(self.dataset[self.data_name].get(str(serial_class_number), [])[0], 1))

    def get_data_sample(self, serial_class_number: int, serial_data_number: int):
        """
        Возвращает данные для текущего изображения.

        :param serial_class_number: Порядковый номер класса данных.
        :param serial_data_number: Номер данных, для которых нужно нормированное значение.

        :return: Данные для текущего изображения.
        """
        result = self.get_data_dict(serial_class_number).get(serial_data_number)
        if result is None:
            raise ValueError(f'Номер {serial_data_number} или номер {serial_class_number} за пределами диапазона!')
        return result

    def create_output_layer_data(self, output_layer: list[float], file_exist: bool = True) -> None:
        """
        Создаёт словарь с выходными данными.

        :param output_layer: Список выходных данных.
        :param file_exist: Флаг наличия или отсутствия файла выходных данных.
        """
        output_layer_data: dict[str, list[float]] = {}
        serial_class_number: int = self.get_data_dict_value('serial_class_number')

        for i in range(serial_class_number):
            if file_exist:
                output_layer_data[str(i + 1)] = output_layer[i::serial_class_number]
            else:
                output_layer_data[str(i + 1)] = [0.0 * self.get_data_dict_value('serial_data_number')]
        save_json_data('memory/mto_weights', 'output_layer_data', output_layer_data)

    def load_output_layer_data(self, init_network) -> list[float]:
        """
        Загружает сохранённые выходные данные.

        :param init_network: Ссылка на функцию инициализации нейросети.
        """
        output_layer_data: list[float] = []

        for _ in range(self.get_data_dict_value('serial_data_number')):
            for _ in range(self.get_data_dict_value('serial_class_number')):
                result: int | float = init_network()
                output_layer_data.append(result)
                self.serial_class_number += 1
            self.serial_class_number: int = 1
            self.serial_data_number += 1

        return output_layer_data


class Classification(SupportFunctions):

    def get_classification(self, output: float, data_dict: dict, key_mode: bool, margin: float = float('inf')) -> str:
        result = None
        min_difference: float = float(self.format_string(margin))
        try:
            for key, value in data_dict.items():
                if key_mode:
                    difference: float = abs(output - float(key))
                else:
                    difference: float = next(abs(output - i) for i in value)
                if difference < min_difference:
                    min_difference = difference
                    result = key
        except FileNotFoundError as e:
            logger.error(f'Произошла ошибка: {e}')
        return result
