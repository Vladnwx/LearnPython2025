Задача 2.
Создать класс. Очередь на структуре данных двусвязный список. 



class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        pass
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        pass

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        pass

    def print(self):
        """
        вывод на печать содержимого очереди
        """
        pass
