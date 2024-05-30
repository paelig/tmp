class Product:
    @classmethod
    def name_author(cls, name):
        return cls.Author(name)

    @classmethod
    def name_creation(cls, name):
        return cls.Creation(name)


class Book(Product):
    class Author:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"The author of this book is {self.name}"

    class Creation:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"The name of this book is {self.name}"

    def __str__(self):
        return "Book"


class Film(Product):
    class Author:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"The director of this film is {self.name}"

    class Creation:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"The name of this film is {self.name}"


def show_dialog(factory):
    author = factory.name_author('Name 1')
    title = factory.name_creation('Name 2')
    print(str(author), str(title), sep='\n')


# Использование
print('Book')
show_dialog(Book)
print('Film')
show_dialog(Film)
