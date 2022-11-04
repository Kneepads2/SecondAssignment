import Product_2
from Product_2 import *

print("\nWelcome to Dylan's off-brand inventory system!!!!\n")

class Application:
    def __init__(self,code,name,salesPrice,manufactureCost,stock,monthlyUnitsMade,months,unitsSold,totalSold):
        self.code = code
        self.name = name
        self.salesPrice = salesPrice
        self.manufactureCost = manufactureCost
        self.stock = stock
        self.monthlyUnitsMade = monthlyUnitsMade
        self.months = months
        self.unitsSold = unitsSold
        self.totalSold = totalSold
    
    def getProductCode(self): #to get the product code
        while True: #Gathering the product code. Using a while loop and valueErrors to make sure that the input received is not letters or below 100 or above 1000
          try:
              self.code = int(input('What is the code of the product?  '))
              if (self.code < 100 or self.code > 1000):
                   raise ValueError       
              break
          except ValueError:
            print('Please enter the code. It is a number between 100 and 1000.')
    
        return "Code accepted.\n"
    
    def getProductName(self): #to get the product name
        self.name = str(input("What is the name of the product? ")) # No need for the loops since we only need string
        if (self.name == ""): # If they enter nothing, it should make the product name 'Unnamed Product'
            self.name = "Unnamed Product"
        
        return "Name accepted.\n"
        

    def getSalesPrice(self): #to get the sales price per unit
        while True: #Gathering the sales price. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
            try:
                 self.salesPrice = float(input('What is the retail price of the product?  '))
                 if (self.salesPrice < 0):
                      raise ValueError       
                 break
            except ValueError:
                print('Please enter the retail price of your product. You cannot charge people negative dollars. ')
        
        return "Pricing accepted.\n"
        
    
    def getManufactureCost(self): #to get the manufacture cost per unit
        while True: #Gathering the manufacture cost. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
            try:
             self.manufactureCost = float(input('What is the manufacture price of the product?  '))
             if (self.manufactureCost < 0):
                raise ValueError       
             break
            except ValueError:
                print('Please enter the manufacture price of your product. Nothing can cost negative dollars. ')
        
        return "Cost accepted.\n"
    
    def getStockLevel(self):
        while True: #Gathering the stock level. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
           try:
              self.stock = int(input('How much stocks of your product do you have right now?  '))
              if (self.stock < 0):
                 raise ValueError       
              break
           except ValueError:
                print('There\'s no way you have that amount of stock. Please enter how much stock you have.  ')
        
        return "Stock level confirmed.\n"
    
    def getMonthlyProduction(self): # to get the estimiated monthly production
        while True: #Gathering the stock level. Using a while loop and valueErrors to make sure that the input received is not letters or below 0 
             try:
                self.monthlyUnitsMade = int(input('How many products can you manufacture per month.  '))
                if (self.monthlyUnitsMade < 0):
                  raise ValueError       
                break
             except ValueError:
                 print('Impossible.  ')
        
        return "Estimated Monthly production confirmed.\n"
    
    def run(self): #i have placed Product_2.Statement() in here because I cannot place the variables in this class outside of the class so this is why run exists
        p = Product_2.Statement(self.code,self.name,self.salesPrice,self.manufactureCost,self.stock,self.monthlyUnitsMade,12,0,0)
        print(p.predictedStockStatement())
        print(p.netProfitOrLoss(12))
        return "\n***********************************"
    
    #to be able to print everything
q = Application(0,"",0,0,0,0,12,0,0)

print(q.getProductCode())
print(q.getProductName())
print(q.getSalesPrice())
print(q.getManufactureCost())
print(q.getMonthlyProduction())
print(q.getStockLevel())
print(q.run())