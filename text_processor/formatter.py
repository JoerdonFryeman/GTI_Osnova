import re


class TextFormatting:

    @staticmethod
    def process_text(words_list: list[str]) -> str:
        """
        Обрабатывает список слов и форматирует текст.

        :param words_list: Список слов, который будет объединён в строку.
        :return: Отформатированная строка текста с правильными пробелами и заглавными буквами в начале предложений.
        """
        text: str = ' '.join(words_list)
        text: str = re.sub(r'\s*-\s*', '-', text)
        text: str = re.sub(r'\s+([!?.,:;])', r'\1', text)
        sentences: list[str] = re.split(r'(?<=[!?.])\s+', text)
        capitalized_sentences: list[str] = [s.capitalize() for s in sentences]
        return ' '.join(capitalized_sentences)

    @staticmethod
    def separate_text(text: str, group_size: int = 13) -> str:
        """
        Разделяет текст на группы слов заданного размера.

        :param text: Исходный текст, который подлежит разделению.
        :param group_size: Количество слов в одной группе (по умолчанию 13).
        :return: Строка, состоящая из строк групп слов, разделённых переводами строки.
        """
        words: list[str] = text.split()
        parts: list[str] = [' '.join(words[i:i + group_size]) for i in range(0, len(words), group_size)]
        return '\n'.join(parts)
