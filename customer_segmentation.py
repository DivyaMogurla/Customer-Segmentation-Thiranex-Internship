import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = {
    "Customer_ID": [f"C{1001+i}" for i in range(n)],
    "Age": np.random.randint(18, 65, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Income": np.random.randint(20000, 150000, n),
    "Purchase_Frequency": np.random.randint(1, 20, n),
    "Total_Spending": np.random.randint(500, 50000, n),
    "Average_Order_Value": np.random.randint(200, 5000, n),
    "Website_Visits": np.random.randint(1, 30, n),
    "Discount_Usage": np.random.randint(0, 15, n)
}

df = pd.DataFrame(data)

df.to_csv("customer_data.csv", index=False)

print("Customer dataset created successfully!")
print(df.head())
print("\nDataset shape:", df.shape)