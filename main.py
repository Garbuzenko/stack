

# Press the green button in the gutter to run the script.
from Stack import Stack

open = '({['
close = ')}]'

def get_open_by_close(c):
    return open[close.index(c)]

def check_string(s_input):
    stack = Stack()
    for s in s_input:
        if s in open:
            stack.push(s)
        if s in close:
            if stack.isEmpty():
                return False
            if get_open_by_close(s) != stack.pop():
                return False
    return True

if __name__ == '__main__':
    s_input = str(input('Введите строку со скобками ' + open + close + ':'))
    if check_string(s_input) == True:
        print("Сбалансированно")
    else:
        print("Несбалансированно")
