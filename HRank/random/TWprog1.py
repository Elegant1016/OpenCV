#Author : R Santosh Kumar
#Date : 17 Aug 2016
#Program Name : Discounts on apparel



class HyderabadCentral:
    def __init__(self):
        #Dictionary that maps Parent Category
        self.catDiscount = {"Mens" : None, "Womens" : 50}

        #Dictionary that maps items-category
        self.itemDiscount = {
                        "Mens" : {"Shirts" : None, "Trousers": None, "Casuals": 30, "Jeans":20},
                        "Womens" : {"Dresses" : None, "Footwear" : None}
                      }
        #Dictionary that maps brand discount
        self.brandDiscount = {"Wrangler" :10, "Arrow" :20, "Vero Moda" : 60, "UCB" :None, "Adidas" :5, "Provogue" :20}

        #Dictionary that maps buyers selection
        self.choiceDict = dict()


    def maxDiscount(self,brand, cat, price):
        discount1 = discount2 = discount3=None

        discount1 = self.brandDiscount[brand.strip()]
        category = cat.strip()
        if category in self.itemDiscount["Mens"].keys():
            discount2 = self.itemDiscount["Mens"][category]
            discount3 = self.catDiscount["Mens"]
        elif category in self.itemDiscount["Womens"].keys():
            discount2 = self.itemDiscount["Womens"][category]
            discount3 = self.catDiscount["Womens"]

        if discount1 == None:
            discount1 = 0
        if discount2 == None:
            discount2 = 0
        if discount3 == None:
            discount3 = 0

        rebate = 100 - max(discount1, discount2, discount3)
        return rebate

    def calculateBill(self, items):
        total = 0
        for i in items:
            total = total + self.choiceDict.get(i)
        print(total)



if __name__ == "__main__":
    biller = HyderabadCentral()

    # User input for the choices of items to buy
    choice = int(input())

    for i in range(1, choice + 1):
        discount1 = discount2 = discount3 = None
        id, brand, cat, price = input().strip().split(",")
        rebate = biller.maxDiscount(brand, cat, price)
        p = (rebate * int(price)) / 100
        biller.choiceDict[i] = int(p)

    # Finals items which user wants to buy
    bought = int(input())

    for i in range(bought):
        items = [int(i) for i in input().split(',')]
        biller.calculateBill(items)


''' Test Case
5
1, Arrow,Shirts,800
2, Vero Moda,Dresses,1400
3, Provogue,Footwear,1800
4, Wrangler,Jeans,2200
5, UCB,Shirts,1500
2
1,2,3,4
1,5
'''