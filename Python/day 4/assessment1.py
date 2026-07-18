class book :
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_details(self):
        print("title:",self.title)
        print("author:",self.author)
        print("price:",self.price)
    def update_price(self,new_price):
        self.price=new_price
        print("updated price:",new_price)
    def discount_percent(self,percent):
        self.price=self.price-(self.price*percent/100)
        print("discounted price:",self.price)
book1=book("wings of fire","apj abdul kalam",500)
book2=book("rich dad poor dad","robert kiyosaki",600)
book3=book("the monk who sold his ferrari","robin sharma",700)

book1.display_details()
book2.display_details()
book3.display_details()

book1.update_price(550)
book2.update_price(650)
book3.update_price(750)

book1.discount_percent(10)
book2.discount_percent(20)
book3.discount_percent(30)
    
        
    
