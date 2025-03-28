# Задача 2.
# Создать класс. Очередь на структуре данных двусвязный список.
print("\033c", end="")


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
    Реализуется по принципу FIFO
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        Проверим что очередь не пустая
        1. Запишем значение из начала во временную переменную
        2. Переместим указатель очереди на следующий объект
        3. Вернем временную переменную
        """
        if self.start != None:
            temp = self.start.data
            self.start = self.start.nref
            print(f"Элемент {temp} извлечен из очереди")
            return temp
        else:
            print("Очередь пустая")
            return None

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        tempNode = Node(val)
        #print(f"Элемент {val} создан новый узел")

        if self.start == None:
            print("Очередь пустая")
            self.start = tempNode
            self.end = tempNode
        else:
            self.end.nref = tempNode
            tempNode.pref = self.end
            self.end = tempNode

        print(f"Элемент {val} помещён в очередь")

    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        if n <= 0:
            print("Номер элемента для вставки должен быть больше нуля")
            return None
        elif self.start == None:
            self.push(val)
            return
        elif n == 1:
            tempNode = Node(val)
            #print(f"Элемент {val} создан новый узел")
            # Поиск элемента куда нужно вставить              
            tmp = self.start #Сохраняем указатель на следующий элемент
            self.start = tempNode # Найденному элементу присваиваем указатель на следующий элемент -> tempNode
            tempNode.nref = tmp # tempNode указывает на следующий элемент
        else:
            count = 1
            current = self.start
            while current != None:
                current = current.nref
                count += 1
            if n >= count - 1:
                print(
                    "Номер элемента для вставки больше размера очериди и будет помещен в конец очереди"
                )
                self.push(val)
            else:
                tempNode = Node(val)
                #print(f"Элемент {val} создан новый узел")
                # Поиск элемента куда нужно вставить
                ptr = self.start  # указатель на начало очереди
                i = 1  # текущий элемент
                while i < n-1:  # Ищем элемент n-1
                    ptr = ptr.nref  # Переходим по списку на следующий элемент
                    i += 1
                
                tmp = ptr.nref #Сохраняем указатель на следующий элемент
                ptr.nref = tempNode # Найденному элементу присваиваем указатель на следующий элемент -> tempNode
                tempNode.nref = tmp # tempNode указывает на следующий элемент
                tempNode.pref = ptr # tempNode указывает на предыдущий элемент

    def print(self):
        print("Печать содержимого очереди")
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.nref
        print()


def test():
    queue = Queue()
    queue.push(1)
    queue.pop()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.print()
    queue.pop()
    queue.print()
    queue.push(4)
    queue.push(5)
    queue.insert(42, 6)
    queue.print()


test()
