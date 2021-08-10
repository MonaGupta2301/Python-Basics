class library:
    def __init__(self,booksName):
        self.Books=booksName

    def displayBooks(self):
        for Books in self.Books:
            print(Books)

class student:
    pass


if __name__ == "__main__":
    l=("c++","java","Python","Harypatter","jango")
    dis=library(l)
    dis.displayBooks()