import numpy as np
import matplotlib
# %matplotlib inline
# Or %matplotlib notebook

data = pd.DataFrame(data=np.random.rand(4, 4) * 100000, 
                    index=["Q1", "Q2", "Q3", "Q4"],
                    columns=["East", "West", "North", "South"])

data.index.name = "Quarters"
data.columns.name = "Region"
data

print(data)