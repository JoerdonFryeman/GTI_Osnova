import re

from base.support_functions import SupportFunctions


class TextEncoder(SupportFunctions):

    def get_text_cleaner(self, character: str) -> str:
        """
        Очищает текст от нежелательных символов и приводит к нижнему регистру.

        :param character: Строка, которую необходимо очистить.
        :return: Очищенная строка в нижнем регистре.
        :raises Exception: Если знак препинания находится в списке исключений.
        """
        for i in self.punctuation_characters:
            if i in self.unwanted_characters:
                raise Exception(f'Знак препинания "{i}" находится в списке исключений "unwanted_characters"!')
        pattern: str = f'[{re.escape(self.unwanted_characters)}]+'
        return re.sub(pattern, '', character).lower()

    def get_encoded_sentence(self, dictionary: dict[str, str], sentence: str) -> list[float | KeyError]:
        """
        Кодирует предложение с использованием заданного словаря.

        :param dictionary: Словарь для кодирования, где ключи - слова, а значения - кодировки.
        :param sentence: Исходное предложение, которое необходимо закодировать.
        :return: Список кодов для каждого слова в предложении или KeyError, если код не найден.
        """
        reversed_dict: dict[str, str] = {value: key for key, value in dictionary.items()}
        words_and_punctuation: list[str] = re.findall(rf'\w+|[{re.escape(self.punctuation_characters)}]', sentence)
        encoded_values: list[float | KeyError] = []

        for word in words_and_punctuation:
            cleaned_word: str = self.get_text_cleaner(word)
            try:
                encoded_values.append(float(reversed_dict[cleaned_word]))
            except KeyError as key:
                encoded_values.append(key)

        return encoded_values
