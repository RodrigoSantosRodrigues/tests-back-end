from enum import Enum


class OperationEnum(str, Enum):
    addPoint = 'addPoint'
    removePoint = 'removePoint'
    end = 'end'
