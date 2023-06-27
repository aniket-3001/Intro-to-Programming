class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Member:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)


class BookClub:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def find_book(self, book):
        for member in self.members:
            if book in member.books:
                return member

    def transfer_book(self, m1, m2, book):
        m1.remove_book(book)
        m2.add_book(book)


if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10)
    book2 = Book("The Catcher in the Rye", "J. D. Salinger", 8)
    book3 = Book('The 4-Hour Workweek', 'Tim Ferriss', 15)
    book4 = Book('The Lean Startup', 'Eric Ries', 10)
    book5 = Book('The 7 Habits of Highly Effective People', 'Stephen Covey', 5)
    book6 = Book('The Business School', 'Robert Kiyosaki', 25)

    member1 = Member("David", [book2])
    member2 = Member("Aaron", [book3, book4, book5])
    member3 = Member("Emily", [book1, book6])

    book_club = BookClub("IIITD Book Club", [])
    book_club.add_member(member1)
    book_club.add_member(member2)
    book_club.add_member(member3)

    book = book1
    member = book_club.find_book(book)
    print(member.name)  # Emily
    book_club.transfer_book(member3, member2, book)
    member = book_club.find_book(book)
    print(member.name)  # Aaron
