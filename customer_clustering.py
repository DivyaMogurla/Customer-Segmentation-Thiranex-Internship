import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD DATASET
# ==========================================

df = pd.read_csv("customer_data.csv")

# ==========================================
# STEP 2: SELECT FEATURES
# ==========================================

features = [
    "Age",
    "Income",
    "Purchase_Frequency",
    "Total_Spending",
    "Average_Order_Value",
    "Website_Visits",
    "Discount_Usage"
]

X = df[features]

print("Selected Features:")
print(features)

print("\nOriginal Data Shape:")
print(X.shape)

# ==========================================
# STEP 3: STANDARDIZE FEATURES
# ==========================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled Data Shape:")
print(X_scaled.shape)

print("\nFirst 5 Scaled Records:")
print(X_scaled[:5])

# ==========================================
# STEP 4: ELBOW METHOD
# ==========================================

inertia = []

for k in range(2, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

print("\nInertia Values:")

for k, value in zip(range(2, 11), inertia):
    print(f"K = {k}: Inertia = {value:.2f}")

# ==========================================
# STEP 5: ELBOW GRAPH
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(
    range(2, 11),
    inertia,
    marker='o'
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal K")
plt.xticks(range(2, 11))
plt.grid(True)

plt.show()

# ==========================================
# STEP 6: K-MEANS CLUSTERING
# ==========================================

optimal_k = 5

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# ==========================================
# STEP 7: CLUSTER INFORMATION
# ==========================================

print("\nCustomer Cluster Counts:")

print(
    df["Cluster"]
    .value_counts()
    .sort_index()
)

print("\nFirst 10 Customers with Cluster:")

print(
    df[features + ["Cluster"]]
    .head(10)
)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Elbow Method
inertia = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

print("\nElbow Method Results:")
for k, value in zip(range(2, 11), inertia):
    print(f"K = {k}, Inertia = {value:.2f}")

# Step 8: Final K-Means Clustering

optimal_k = 5

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nFinal Customer Segments:")
print(df["Cluster"].value_counts().sort_index())

print("\nFirst 10 Customers with Final Clusters:")
print(df.head(10))

# Save clustered dataset
df.to_csv("customer_segmented.csv", index=False)

print("\nCustomer segmentation completed successfully!")
print("Saved as: customer_segmented.csv")


# STEP 8: FINAL CUSTOMER SEGMENTATION

optimal_k = 5

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nFinal Customer Segments:")
print(df["Cluster"].value_counts().sort_index())

print("\nFirst 10 Customers with Final Clusters:")
print(df.head(10))

df.to_csv("customer_segmented.csv", index=False)

print("\nCustomer segmentation completed successfully!")
print("Saved as: customer_segmented.csv")
# ==========================================
# STEP 9: ANALYZE CUSTOMER SEGMENTS
# ==========================================

segment_analysis = df.groupby("Cluster")[features].mean().round(2)

print("\nCustomer Segment Analysis:")
print(segment_analysis)

# Save segment analysis
segment_analysis.to_csv("segment_analysis.csv")

print("\nSegment analysis saved as: segment_analysis.csv")
# ==========================================
# STEP 10: CUSTOMER SEGMENT VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt

# Cluster size chart
cluster_counts = df["Cluster"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(cluster_counts.index.astype(str), cluster_counts.values)
plt.xlabel("Customer Cluster")
plt.ylabel("Number of Customers")
plt.title("Customer Distribution by Cluster")
plt.show()

# Income by cluster
plt.figure(figsize=(8, 5))
plt.bar(
    segment_analysis.index.astype(str),
    segment_analysis["Income"]
)
plt.xlabel("Customer Cluster")
plt.ylabel("Average Income")
plt.title("Average Income by Customer Cluster")
plt.show()

# Average Order Value by cluster
plt.figure(figsize=(8, 5))
plt.bar(
    segment_analysis.index.astype(str),
    segment_analysis["Average_Order_Value"]
)
plt.xlabel("Customer Cluster")
plt.ylabel("Average Order Value")
plt.title("Average Order Value by Customer Cluster")
plt.show()
# ==========================================
# STEP 11: CUSTOMER SEGMENT INTERPRETATION
# ==========================================

print("\n==========================================")
print("STEP 11: CUSTOMER SEGMENT INTERPRETATION")
print("==========================================")

segment_names = {
    0: "High Income - Moderate Engagement",
    1: "Frequent Buyers - Lower Income",
    2: "High Website Visitors - Low AOV",
    3: "Young - High Income Customers",
    4: "High Value - High Website Visitors"
}

for cluster, name in segment_names.items():
    print(f"Cluster {cluster}: {name}")

print("\nCustomer Segment Summary:")
print(segment_analysis)
# ==========================================
# STEP 12: BUSINESS RECOMMENDATIONS
# ==========================================

print("\n==========================================")
print("STEP 12: BUSINESS RECOMMENDATIONS")
print("==========================================")

recommendations = {
    0: "Offer premium products and personalized offers to higher-income customers.",
    1: "Use loyalty programs and targeted discounts to encourage frequent purchases.",
    2: "Use product recommendations and promotional campaigns to convert website visits into purchases.",
    3: "Promote premium products and personalized marketing to younger, higher-income customers.",
    4: "Focus on premium products, cross-selling, and personalized recommendations for high AOV customers."
}

for cluster, recommendation in recommendations.items():
    print(f"Cluster {cluster}: {recommendation}")