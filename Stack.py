from queue import LifoQueue
class Stack(object):
    def __init__(self):
        self.queue = []

    # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        return len(self.queue) == 0

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, item):
        self.queue.append(item)

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.queue.pop()

    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peak(self):
        return self.queue[-1]

    # size - возвращает количество элементов в стеке.'
    def size(self):
        return len(self.queue)



