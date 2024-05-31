# Базовый компонент
class Component:
    def operation(self):
        pass


# Лист (лист дерева)
class Leaf(Component):
    def __init__(self, task) -> None:
        self.task = task

    def print_(self):
        print(f"Лист: {self.task}")


# Контейнер (узел дерева)
class Unit(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def print_(self):
        print("Блок: Выполнение операции")
        for child in self.children:
            child.print_()


# Использование
leaf1 = Leaf('Задача 1')
leaf2 = Leaf('Задача 2')
leaf3 = Leaf('Задача 3')
composite = Unit()

composite.add(leaf1)
composite.add(leaf2)
composite.add(leaf3)

composite.print_()
