class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybook(self):
        print('We have following books in {self.name} library.')
        for book in self.booklist:
              print(book)

    def lendbook(self, book, user):
        if book not in self.lendDict.keys():
            self.lendDict.update({name:user})
            print('Lend book dictionary is updated. You can take the book.')
        else:
            print('Book is not available')

    def addbook(self, book):
        self.booklist.append(book)
        print('Book is added.')

    def returnbook(self, book):
        self.booklist.remove(book)
        print('Book is returned.')

    
       
if __name__ == '__main__':
  MyLibrary = Library(['Statistics', 'C++ Basics', 'Python Programming', 'The Alchemist'],['Anitabook'])

  while(True):
    print('Welcome to the library.\n Enter your choice')
    print('1. Display the list of books.')
    print('2. Lend a book.')
    print('3. Add a book.')
    print('4. Return a book.')
    mynumber = input()
    if mynumber not in '1' '2' '3' '4' 'q' 'c':
      print('Enter a valid number.')
      continue
    elif mynumber in 'c' 'q':
      mynumber = mynumber
    else:
      mynumber = int(mynumber)

    if mynumber == 1:
      MyLibrary.displaybook()

    elif mynumber == 2:
      name =input('Enter the book name: ')
      user = input('Enter the name of user: ')
      MyLibrary.lendbook(name, user)

    elif mynumber == 3:
      name = input('Enter The name of book: ')
      MyLibrary.addbook(name)

    elif mynumber == 4:
      name = input('Enter the name of the book to be returned: ')
      MyLibrary.returnbook(name)

    elif mynumber == "q":
      break
      
    elif mynumber == "c":
      continue
    

    
