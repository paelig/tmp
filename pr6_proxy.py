class Proxy:
    def __init__(self, title):
        self.client = Client1(title)

    def set_title(self, title, pas):
        if pas == '1234':
            print('Change title')
            print(self.client.set_title(title))
        else:
            print(f"Error! Password {pas} is wrong")

    def print_(self, pas):
        if pas == '1234':
            print('You use Proxy!', self.client)
        else:
            print(f"Error! Password {pas} is wrong")


class Client1(Proxy):
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"I'm Client1, my name is {self.title}"

    def set_title(self, title):
        self.title = title
        return self


# Использование
print(Client1('1234'))

cl = Proxy('1234')
cl.print_('234')
cl.print_('1234')

cl.set_title('457', '123')
cl.set_title('457', '1234')
