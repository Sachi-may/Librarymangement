class Library:
    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
        self.lend_data={}


    def displaybook(self):
        print(f"The name of our library is {self.library_name} and the books available in our library are")
        for books in self.list_of_books:
            print(books)
    def lendbook(self,lender,book):
        if book not in self.lend_data.keys():
            self.lend_data.update({book:lender})
            print("Data has been updated. You are ready to land the book")
        else:
            print(f"The book is already being used by {self.lend_data[book]}")
    def returnbook(self,book):
        self.lend_data.pop(book)
        print("The book is returned sucessfully")

    def addbook(self,book):
        self.list_of_books.append(book)
        print("The book is added successfully")
    def removebook(self,book):
        self.list_of_books.remove(book)
        print("The book is removed succesfully")


if __name__ == '__main__':
    obj=Library(["Rich dad poor dad","Python","C++ basics","Chetan bhagat","Tin goyenda"],"SS Library")
    while (True):
        print("Choose a option for service\n")
        print("1.Display books")
        print("2.lend book")
        print("3.Return book")
        print("4.Add a book")
        print("5.Removing a book")
        i=int(input())
        if i==1:
            obj.displaybook()
        elif i==2:
            b = input("Enter the book name")
            n = input("Enter your name")
            obj.lendbook(n,b)
        elif i==3:
            b=input("Enter the book name which you want to return")
            obj.returnbook(b)
        elif i==4:
            b=input("Enter the book name which you want to add")
            obj.addbook(b)
        elif i ==5:
            p= 12345
            pa=int(input("Enter the passcode"))
            if pa==p:
                b=input("Enter the book name you want to remove")
                obj.removebook(b)
        else:
            print("Invalid choice")

        print("Press q to quit and c to continue\n")
        j=""
        while(j!="q" and j!= "c"):
            j=input()
            if j=="q":
                exit()
            elif j=="c":
                continue
