# Названия файлов
# Задача 1.
# Создать класс. Стек на структуре данных односвязный список.
print("\033c", end="")

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
    Реализуется по принципу FIFO
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        Проверим что стек не пустой
        1. Запишем значение во временную переменную
        2. Переместим указатель стека на предыдущий объект
        3. Вернем временную переменную
        """
        if self.end != None:
            temp = self.end.data
            self.end = self.end.pref
            print(f"Элемент {temp} извлечен из стека")
            return temp
        else:
            print("Стек пустой")

    def push(self, val):
        """
        добавление элемента val в конец списка
        1. Создание нового элемента узла
        2. Запись в новый элемент узла значения указывающего на вершину стека
        3. Обновление указателя вершины стека на значение нового узла
        """
        tempNode = Node(val)
        print(f"Элемент {val} создан новый узел")
        tempNode.pref = self.end
        self.end = tempNode
        print(f"Элемент {val} помещён в стек")

    def print(self):
        """
        вывод на печать содержимого стека
        """
        print("Печать содержимого стека")
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()


def test():
    stack = Stack()
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()
    stack.pop()
    stack.print()


test()
