from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def work(self, mass):
        pass


class Context:
    strategy: Strategy

    def chooseStrategy(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Strategy2()

    def do_work(self, x):
        print(self.strategy.work(x))


class Strategy1(Strategy):
    def work(self, x: str):
        return "Строка: Стратегия 1"


class Strategy2(Strategy):
    def work(self, x: int):
        return "Число: Стратегия 2"


# Использование
A = Context()
B = Context()

A.chooseStrategy(Strategy1())
B.chooseStrategy()

A.do_work("0987")
B.do_work(9876)
