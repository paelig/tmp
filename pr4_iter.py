class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_num < 0:
            if self.num > self.max_num:
                self.num -= 1
                return self.num
            else:
                raise StopIteration
        else:
            if self.num < self.max_num:
                self.num += 1
                return self.num
            else:
                raise StopIteration


# Использование итератора
print([i for i in MyIterator(21)])
print([i for i in MyIterator(-21)])
