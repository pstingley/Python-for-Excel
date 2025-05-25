import pandas as pd


data = [["Oranges", "North", 12.39],
        ["Apples", "South", 10.55],
        ["Oranges", "South", 22.00],
        ["Bananas", "South", 5.90],
        ["Bananas", "North", 31.30],
        ["Oranges", "North", 13.10]]

sales = pd.DataFrame(data = data, columns=["Fruit", "Region", "Revenue"])
print(sales)