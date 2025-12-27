from random import choice

from text_processor.formatter import TextFormatting
from text_processor.encoder import TextEncoder
from .data import Classification
from .layers import Attention


class ContextProcessor(TextEncoder, Attention):
    pass


class TextGenerator(TextFormatting, Classification, ContextProcessor):
    pass
