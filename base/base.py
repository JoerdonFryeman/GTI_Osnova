import os
import json
from logging import config, getLogger


def get_json_data(directory: str, name: str) -> dict:
    """
    Возвращает данные в формате json из указанного файла.

    :param directory: Название каталога.
    :param name: Имя файла без расширения.
    :return: Словарь с данными из json файла.
    """
    file_path: str = os.path.join(directory, f'{name}.json')
    try:
        with open(file_path, encoding='UTF-8') as json_file:
            data: dict = json.load(json_file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл не найден: {file_path}')
    except json.JSONDecodeError:
        raise ValueError(f'Ошибка декодирования JSON в файле: {file_path}')
    except PermissionError:
        raise PermissionError(f'Нет доступа к файлу: {file_path}')
    except Exception as e:
        raise Exception(f'Произошла ошибка: {str(e)}')


def save_json_data(directory: str, name: str, data: list | dict) -> None:
    """
    Сохраняет файл json.

    :param directory: Директория сохраняемого файла.
    :param name: Имя сохраняемого файла.
    :param data: Данные сохраняемого файла.
    """
    file_path: str = os.path.join(directory, f'{name}.json')
    try:
        with open(file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except PermissionError:
        raise PermissionError(f'Нет доступа для записи в файл: {file_path}')
    except IOError as e:
        raise IOError(f'Ошибка записи в файл: {file_path}. Причина: {str(e)}')
    except Exception as e:
        raise Exception(f'Произошла ошибка: {str(e)}')


def get_method_info(cls, key: str) -> str:
    """
    Логирует информацию о методе класса, включая его имя и документацию.

    :param cls: Класс, вызываемого метода.
    :param key: Ключ, соответствующий методу в словаре класса.
    :return: None. Метод не возвращает значения, а только выполняет логирование.
    """
    return f'Метод {cls.__dict__[key].__name__} класса {cls.__name__}\n{cls.__dict__[key].__doc__}'


directories: tuple[str, str, str, str, str, str, str] = (
    'memory',
    'memory/dictionary',
    'memory/mtm_weights',
    'memory/mtm_weights/no',
    'memory/mtm_weights/text',
    'memory/mtm_weights/yes',
    'memory/mto_weights'
)

for d in directories:
    try:
        os.mkdir(d)
    except FileExistsError:
        pass

config.dictConfig(get_json_data('base/configuration/logs', 'logging'))
logger = getLogger()
