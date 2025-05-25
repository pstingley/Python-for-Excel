import numpy as np
import pandas as pd
import plotly.express as px

# Create random data
data = pd.DataFrame(
    data=np.random.rand(4, 4) * 100000,
    index=["Q1", "Q2", "Q3", "Q4"],
    columns=["East", "West", "North", "South"]
)

data.index.name = "Quarters"
data.columns.name = "Region"

# Reset index so that Quarters becomes a column
data_reset = data.reset_index().melt(id_vars="Quarters", var_name="Region", value_name="Value")

# Create interactive bar plot with Plotly
fig = px.bar(data_reset, x="Quarters", y="Value", color="Region", barmode="group",
             title="Quarterly Regional Data", labels={"Value": "Amount ($)"})

fig.show()
