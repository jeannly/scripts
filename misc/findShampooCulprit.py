# I want the ingredients that are unique to each product so I can find
# where my allergies are coming from >:(
from arrayManipulation import removeCommonElements

# Get ingredients from file
shampoo1 = {
    "title": "",
    "ingredients": []
}

shampoo2 = {
    "title": "",
    "ingredients": []
}
with open('shampoo1_ingredients.csv', 'r', encoding="utf-8") as file:
    shampoo1["title"] = file.readline()
    shampoo1["ingredients"] = file.read().split(',')

with open('shampoo2_ingredients.csv', 'r', encoding="utf-8") as file:
    shampoo2["title"] = file.readline()
    shampoo2["ingredients"] = file.read().split(',')

removeCommonElements(shampoo1["ingredients"],shampoo2["ingredients"])
print(f"{shampoo1['title']}")
print(shampoo1["ingredients"])
print(f"{shampoo2['title']}")
print(shampoo2["ingredients"])
