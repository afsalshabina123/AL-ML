items =["book","bag","pen","bread","milk"]
prices ={"book":60,"bag":450,"pen":10,"bread":35,"milk":29}
for item in items:
   print(item,":",prices[item])

prices.update({"book":50})
print("updated price of book:",prices["book"])
items.remove("pen")
prices.pop("pen")
print("updated list:",items)
print("updated list:",prices)
highest_price =max(prices,key=prices.get)
print("highest priced item:",highest_price)
print("price:",prices[highest_price])
total_cost =sum(prices.values())
print("total cost:",total_cost)
for item in items:
    if prices[item] > 100:
        print("price greater than 100:",item, ":", prices[item])

search_item = input("Enter item name: ")
if search_item in prices:
    print(search_item, ":", prices[search_item])
else:
    print("Item not found")







