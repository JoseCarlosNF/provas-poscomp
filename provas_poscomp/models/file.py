from dataclasses import dataclass
from enum import Enum


class FileType(Enum):
    PROVA = 'prova'
    GABARITO = 'gabarito'


@dataclass
class File:
    path: str
    year: str
    type: FileType
