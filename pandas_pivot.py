import pandas as pd


data = [["Oranges", "North", 12.30],
        ["Apples", "South", 10.55],
        ["Oranges", "South", 22.00],
        ["Bananas", "South", 5.90],
        ["Bananas", "North", 31.30],
        ["Oranges", "North", 13.10]]

sales = pd.DataFrame(data = data, columns=["Fruit", "Region", "Revenue"])
print(sales)
print("\n Pivot Table: ")

pivot = pd.pivot_table(sales,
                       index = "Fruit", columns="Region",
                       values="Revenue", aggfunc="sum", 
                       margins= True, margins_name="Total")

print(pivot)