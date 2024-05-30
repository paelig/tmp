class Mediator:
    def __init__(self):
        self.colleague1 = Entity1(self)
        self.colleague2 = Entity2(self)

    def notify(self, sender, event):
        if sender == self.colleague1:
            print("Entity1 отправил событие:", event)
            self.colleague2.handle_event(event)
        elif sender == self.colleague2:
            print("Entity2 отправил событие:", event)
            self.colleague1.handle_event(event)


class Entity1:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_event(self, event):
        self.mediator.notify(self, event)

    def handle_event(self, event):
        print("Entity1 обработал событие:", event)


class Entity2:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_event(self, event):
        self.mediator.notify(self, event)

    def handle_event(self, event):
        print("Entity2 обработал событие:", event)


# Использование
mediator = Mediator()
mediator.colleague1.send_event("Событие от Entity1")
mediator.colleague2.send_event("Событие от Entity2")
