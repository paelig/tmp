class Service:
    def __init__(self, addiction):
        self.addiction = addiction

    def do_something(self):
        self.addiction.do_stuff()


class Addiction:
    def __init__(self, task) -> None:
        self.task = task

    def do_stuff(self):
        print(self.task)


log_addiction = Addiction('Печать логов')
service = Service(log_addiction)
service.do_something()
work_addiction = Addiction('Работа')
service2 = Service(work_addiction)
service2.do_something()
