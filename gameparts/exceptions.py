class FieldIndexError(IndexError):

    def __str__(self):
        return 'Значение за пределами игрового поля'


class CellOccupiedError(Exception):

    def __str__(self):
        return 'Попытка изменить занятую ячейку'
