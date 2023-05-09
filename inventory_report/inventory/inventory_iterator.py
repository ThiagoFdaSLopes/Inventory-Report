from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, lista):
        self.lista = lista
        self._index = 0

    def __next__(self):
        try:
            current_value = self.lista[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return current_value
