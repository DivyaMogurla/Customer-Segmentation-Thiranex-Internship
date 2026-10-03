# Customer Segmentation using K-Means Clustering

## Thiranex Internship Project

### Project Overview

This project focuses on customer segmentation using the K-Means clustering
algorithm. Customers are grouped based on their demographic, purchasing,
spending, website activity, and discount usage behavior.

## Objective

The main objective of this project is to identify different customer segments
and understand their characteristics to support targeted business strategies.

## Dataset

The dataset contains 500 customer records and includes the following features:

- Customer ID
- Age
- Gender
- Income
- Purchase Frequency
- Total Spending
- Average Order Value
- Website Visits
- Discount Usage

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Project Methodology

1. Loaded the customer dataset
2. Inspected the dataset
3. Selected relevant numerical features
4. Standardized the features using StandardScaler
5. Applied the Elbow Method
6. Selected 5 clusters
7. Applied K-Means clustering
8. Analyzed the customer segments
9. Created visualizations
10. Developed business recommendations

## Customer Segments

| Cluster | Customers | Segment |
|---|---:|---|
| 0 | 111 | High Income - Moderate Engagement |
| 1 | 98 | Frequent Buyers - Lower Income |
| 2 | 95 | High Website Visitors - Low AOV |
| 3 | 92 | Young - High Income |
| 4 | 104 | High Value - High Website Visitors |

## Business Recommendations

- Offer premium products and personalized offers to higher-income customers.
- Use loyalty programs and targeted discounts for frequent buyers.
- Use product recommendations to convert website visits into purchases.
- Use personalized marketing for younger, higher-income customers.
- Use cross-selling and personalized recommendations for high-AOV customers.

## Project Files

- `customer_data.csv` – Customer dataset
- `customer_analysis.py` – Data analysis
- `customer_clustering.py` – K-Means clustering
- `customer_segmented.csv` – Dataset with assigned clusters
- `segment_analysis.csv` – Cluster-level analysis

## Conclusion

K-Means clustering was used to divide 500 customers into five customer
segments based on their characteristics and behavior. The analysis provides
useful insights that can support customer-focused marketing strategies.

## Internship

**Thiranex Internship – Customer Segmentation Project**