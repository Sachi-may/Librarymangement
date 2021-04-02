class library():
    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
        self.lend_data={}

        for books in self.list_of_books:
            self.lend_data[books]=None
    def display(self):
        for books in self.list_of_books:
            print(f"{books}")
    def for_lending(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book]=reader
            else:
                print(f"SORRY! This book is lended by {self.lend_data[book]}")
        else:
            print("Sorry!,BOOK doesnt exist.")

    def return_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry this book is not lended")
        else:
            print("Wrong book")
    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name]=None
    def delete_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

def sachi():
     book_list=["Chacha choudhury","Rich dad poor dad","An angry owl","Timefinisher","Tenet","The wolve"]
     libraryname ="The royal library"
     secret_key=10980

     obj1=library(book_list,libraryname)
     print(f"Welcome to {obj1.library_name} \n Q for quiting the options \nL for lending books \nR for returning the book \nA for adding the book \nD for deleting the book\n Dis for display")

     Exit = False
     while (Exit is not True):
         _input1=input("Options::")


         if _input1 == "Q":
            Exit=True
         elif _input1=="Dis":
            obj1.display()
         elif _input1== "L":
             _input2=input("Enter the book name\n")
             _input3=input("Enter the lender name\n")
             obj1.for_lending(_input2,_input3)
         elif _input1=="R":
             _input2=input("Enter the book name for returning\n")
             _input3=input("Enter the name who is going to return the book\n")
             obj1.return_book(_input2,_input3)
         elif _input1=="A":
             _input2=input("Enter the book name to add\n")
             obj1.add_book(_input2)

         elif _input1=="D":
                n=int(input("Write the secret key to delete"))
                if n==secret_key:
                    _input2=input("Enter the book name to delete\n")
                    obj1.delete_book(_input2)
                else:
                    print("Wrong code")


         else:
             print("Invalid Input")
if __name__=="__main__":
    sachi()
