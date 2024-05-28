class Visitor:
    def visit(self, element):
        pass


class VisitorA:
    def accept(self, visitor):
        visitor.visit(self)


class VisitorB:
    def accept(self, visitor):
        visitor.visit(self)


class ConcreteVisitor(Visitor):
    def visit(self, element):
        if isinstance(element, VisitorA):
            print("Visitor is processing VisitorA")
        elif isinstance(element, VisitorB):
            print("Visitor is processing VisitorB")


# Использование посетителя
a = VisitorA()
b = VisitorB()

visitor = ConcreteVisitor()

a.accept(visitor)
b.accept(visitor)
