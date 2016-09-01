meal = float(input())
tip = int(input())
tax = int(input())

cost = meal + (meal*tip)/100 + (meal*tax)/100
print(cost)
print("The total meal cost is %d dollars." %(int(round(cost))))