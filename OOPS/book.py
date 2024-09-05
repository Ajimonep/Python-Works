class Book:
    title:str
    author:str
    price:int
    language:str
     
    def __init__(self,title,author,price,language):
        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def display_detail(self):
        print(self.title,self.author,self.price,self.language)

    def __str__(self):
        return self.title

book_instance=Book("GOAT LIFE","Benyam",200,"English")

book_instance.display_detail()

print(book_instance) 
 