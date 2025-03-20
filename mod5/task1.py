# Названия файлов
Задача 1.
Создать класс. Стек на структуре данных односвязный список. 
class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        pass
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        pass

    def print(self):
        """
        вывод на печать содержимого стека
        """
        pass

class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            raise IndexError("Попытка извлечь элемент из пустого стека")
        
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()  # Вывод: 3 2 1
print(stack.pop())  # Вывод: 3
stack.print()  # Вывод: 2 1