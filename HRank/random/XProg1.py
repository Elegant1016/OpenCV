#Author : R Santosh Kumar
#Date : 17 Aug 2016
#Program Name : Discounts on apparel

#Dictionary that maps Parent Category
catDiscount = {"Mens" : None, "Womens" : 50}

#Dictionary that maps items-category
itemDiscount = {
                "Mens" : {"Shirts" : None, "Trousers": None, "Casuals": 30, "Jeans":20},
                "Womens" : {"Dresses" : None, "Footwear" : None}
              }
#Dictionary that maps brand discount
brandDiscount = {"Wrangler" :10, "Arrow" :20, "Vero Moda" : 60, "UCB" :None, "Adidas" :5, "Provogue" :20}


#Dictionary that maps buyers selection
choiceDict = dict()

#User input for the choices of items to buy
choice = int(input())

for i in range(1,choice+1):
    discount1 = discount2 = discount3 = None
    id, brand, cat, price = input().strip().split(",")
    discount1 = brandDiscount[brand.strip()]
    category = cat.strip()
    if category in itemDiscount["Mens"].keys():
        discount2 = itemDiscount["Mens"][category]
        discount3 = catDiscount["Mens"]
    elif category in itemDiscount["Womens"].keys():
        discount2 = itemDiscount["Womens"][category]
        discount3 = catDiscount["Womens"]

    if discount1 == None:
        discount1 = 0
    if discount2 == None:
        discount2 = 0
    if discount3 == None:
        discount3 = 0

    rebate = 100 - max(discount1, discount2, discount3)
    p = (rebate * int(price)) / 100
    choiceDict[i] = int(p)

#Finals items which user wants to buy
bought = int(input())

def calculateBill(items):
    total = 0
    for i in items:
        total = total + choiceDict.get(i)
    print(total)

for i in range(bought):
    items = [int(i) for i in input().split(',')]
    calculateBill(items)

'''
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
