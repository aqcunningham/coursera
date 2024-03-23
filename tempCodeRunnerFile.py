class MyFirstClass:
    print('Who wrote this?')
    index = 'Author-Book'

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        # self.philisopher = "Plato"
        # self.book = "Republic"
        
        print(philosopher + " wrote the book: " + book)

#  instantiate an object of that class
whodunnit = MyFirstClass()

# print(whodunnit.hand_list("Sun Tzu", "The Art of War"))
whodunnit.hand_list("Sun Tzu", "The Art of War")


