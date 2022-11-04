
import math
import time
import random
import re

class Statement:

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
    

    def predictedStockStatement(self): #this will print perfectly mimic the predicted stock statement shown in the assignment, figure 1
        print("\n******* Dylan's off-brand inventory system report ******\n")
        print("Product code:  "+ str(self.code))
        print("Product name: "+ str(self.name))
        print("Sales Price: $ {:.2f}".format((self.salesPrice))+" CAD")
        print("Manufacture cost: $ {:.2f}".format((self.manufactureCost))+" CAD")
        print("Current stock level: "+str(self.stock)+" units")
        print("Monthly production: "+str(self.monthlyUnitsMade)+" units (Approx.)")
        counterOne = 0
        
        while (counterOne < self.months):

            self.unitsSold = random.randint(0,int(self.monthlyUnitsMade) + int(self.stock))
            self.stock = (int(self.stock) - int(self.unitsSold) + int(self.monthlyUnitsMade))
            self.totalSold += self.unitsSold
            moneyGained = ((int(self.unitsSold) * float(self.salesPrice)) - (int(self.monthlyUnitsMade) * float(self.manufactureCost) ))
            counterOne += 1

            print ("\nMonth "+ str(counterOne)+ ":\n    Manufactured: "+ str(self.monthlyUnitsMade)+ " units\n    Sold: "+str(self.unitsSold)+ " units\n    Stock: " + str(self.stock)+ " units")
            if (moneyGained < 0):
                print("    Net loss: $ {:.2f}".format(moneyGained)+" CAD")
            else: 
                print("    Net profit: $ {:.2f}".format(moneyGained)+" CAD")
            time.sleep(1)
        return "***********************************\n"
            
    def netProfitOrLoss(self,months2): #this will produce the TOTAL net profit/loss
    # (Total Units Sold * Sale Price) - (Total Units Manufactured * Manufacture Cost).”
    #a number lower than 0 results in Net loss
    #a number higher or equal to 0 results in Net Profit
        moneyGained = ((int(self.totalSold) * float(self.salesPrice)) - (int(self.monthlyUnitsMade) * int(months2) * float(self.manufactureCost) ))
        if (moneyGained < 0):
            
            return("Total Net loss: $ {:.2f}".format(moneyGained)+" CAD")
        else:
            return("Total Net profit: $ {:.2f}".format(moneyGained)+" CAD")


