# 📊 Customer Cohort & Retention Analysis

An end-to-end **Customer Analytics and Retention Analysis project** using **Python, Pandas, Cohort Analysis, RFM Segmentation, and Power BI**.

This project analyzes customer purchasing behavior to identify **retention patterns, customer value, customer segments, and at-risk customers**. The processed data is transformed into Power BI-ready datasets for building an interactive business intelligence dashboard.

---

## 🎯 Project Objective

The objective of this project is to understand customer behavior and answer important business questions:

* How many customers return after their first purchase?
* What is the customer retention rate over time?
* Which customer cohorts have the best retention?
* Which customers generate the most revenue?
* Which customers are at risk of becoming inactive?
* Which customer segments contribute the most revenue?
* How frequently do customers make purchases?
* How recently did customers make their last purchase?
* How can businesses improve customer retention?

---

## 🛠️ Technologies Used

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| **Python**       | Data processing and analysis     |
| **Pandas**       | Data cleaning and transformation |
| **NumPy**        | Numerical operations             |
| **Matplotlib**   | Data visualization               |
| **Seaborn**      | Cohort retention heatmap         |
| **Power BI**     | Interactive dashboard            |
| **DAX**          | Business KPIs and calculations   |
| **Excel**        | Dataset                          |
| **Git & GitHub** | Version control and portfolio    |

---

## 📂 Dataset

This project uses the **Online Retail Dataset** from the UCI Machine Learning Repository.

The dataset contains transactions from a UK-based online retailer between **December 2010 and December 2011**.

### Main columns

| Column        | Description                       |
| ------------- | --------------------------------- |
| `InvoiceNo`   | Unique invoice/transaction number |
| `StockCode`   | Product code                      |
| `Description` | Product description               |
| `Quantity`    | Quantity purchased                |
| `InvoiceDate` | Date and time of transaction      |
| `UnitPrice`   | Price per item                    |
| `CustomerID`  | Unique customer identifier        |
| `Country`     | Customer's country                |

Dataset source:

**UCI Machine Learning Repository — Online Retail Dataset**

---

# 🔄 Project Workflow

```text
                Online Retail Dataset
                         │
                         ▼
                  Data Cleaning
                         │
                         ▼
              Exploratory Data Analysis
                         │
                         ▼
                Revenue Analysis
                         │
                         ▼
              Customer Cohort Analysis
                         │
                         ▼
              Retention Rate Analysis
                         │
                         ▼
                  RFM Analysis
                         │
                         ▼
              Customer Segmentation
                         │
                         ▼
              Power BI Data Preparation
                         │
                         ▼
              Interactive Dashboard
                         │
                         ▼
                Business Insights
```

---

# 🧹 1. Data Cleaning

The raw transaction data is cleaned using Python.

The following preprocessing steps are performed:

* Remove records with missing `CustomerID`
* Remove cancelled invoices
* Remove transactions with zero or negative quantity
* Remove transactions with zero or negative unit price
* Convert `InvoiceDate` to datetime
* Convert `CustomerID` to integer
* Create a new `Revenue` column
* Create an `InvoiceMonth` column

### Revenue Calculation

```python
Revenue = Quantity × UnitPrice
```

---

# 📈 2. Exploratory Data Analysis

The project calculates important business KPIs including:

* Total Revenue
* Total Customers
* Total Orders
* Total Products
* Total Quantity Sold
* Average Order Value

The analysis also examines:

* Monthly revenue
* Monthly customers
* Monthly orders
* Top products
* Revenue by country

---

# 👥 3. Customer Cohort Analysis

A **customer cohort** is a group of customers who made their first purchase during the same month.

For example:

```text
January 2011 Cohort
        │
        ▼
Customers whose first purchase
occurred in January 2011
```

Each customer's first purchase month is identified as their **Cohort Month**.

The project then tracks the customer's activity in subsequent months.

---

# 📊 4. Customer Retention Analysis

Customer retention is calculated by comparing the number of active customers in each month with the number of customers in their original cohort.

Example:

| Cohort   | Month 1 | Month 2 | Month 3 | Month 4 |
| -------- | ------: | ------: | ------: | ------: |
| Jan 2011 |    100% |     35% |     28% |     23% |
| Feb 2011 |    100% |     31% |     25% |     20% |
| Mar 2011 |    100% |     29% |     22% |     18% |

The first month is treated as **100% retention** because it represents the customer's acquisition month.

### Retention Heatmap

The project generates a heatmap showing customer retention across cohorts and months.

```text
                  Months Since First Purchase

              1      2      3      4      5
Jan-2011    100%    35%    28%    23%    19%
Feb-2011    100%    31%    25%    20%    17%
Mar-2011    100%    29%    22%    18%    15%
```

This helps identify cohorts with stronger or weaker long-term retention.

---

# 👤 5. Customer Metrics

Customer-level metrics are calculated using:

### Recency

Number of days since the customer's last purchase.

```text
Lower Recency = More Recently Active
```

### Frequency

Number of unique orders made by the customer.

```text
Higher Frequency = More Frequent Customer
```

### Monetary

Total revenue generated by the customer.

```text
Higher Monetary Value = Higher Customer Value
```

---

# 🧮 6. Customer Status

Customers are classified using their recency:

| Recency    | Status     |
| ---------- | ---------- |
| 0–30 days  | 🟢 Active  |
| 31–90 days | 🟠 At Risk |
| 91+ days   | 🔴 Churned |

These thresholds are used as a practical business rule for this portfolio project.

---

# 💎 7. RFM Analysis

RFM stands for:

### R — Recency

How recently the customer purchased.

### F — Frequency

How frequently the customer purchases.

### M — Monetary

How much the customer spends.

Each customer receives an RFM score and is assigned to a customer segment.

---

# 👥 8. Customer Segmentation

The project identifies the following customer segments:

### 🏆 Champions

Recent, frequent, and high-value customers.

### 💙 Loyal Customers

Customers who purchase regularly and remain engaged.

### 🟢 Potential Loyalists

Recently active customers who have potential to become loyal customers.

### 🟠 At Risk

Previously engaged customers who have not purchased recently.

### 🔴 Lost Customers

Customers with low engagement and long periods since their last purchase.

---

# 📊 Power BI Dashboard

The processed datasets are imported into **Power BI** to create an interactive customer analytics dashboard.

## Dashboard Page 1 — Customer Overview

### KPI Cards

* Total Customers
* Total Revenue
* Total Orders
* Average Order Value
* Repeat Customer Rate

### Visualizations

* Monthly Revenue Trend
* Monthly Customer Trend
* New vs Returning Customers
* Revenue by Country
* Top Products

---

## Dashboard Page 2 — Cohort & Retention

### Main Visualization

**Customer Cohort Retention Heatmap**

Shows:

* Cohort Month
* Months Since First Purchase
* Retention Percentage

### Additional Visualizations

* Customer Retention Trend
* Revenue by Cohort
* Cohort Customer Count
* Retention KPIs

---

## Dashboard Page 3 — RFM Segmentation

### KPI Cards

* Total Customers
* Champions
* Loyal Customers
* Potential Loyalists
* At Risk
* Lost Customers

### Visualizations

* Customers by Segment
* Revenue by Segment
* Average Revenue by Segment
* Recency vs Monetary Value
* Frequency vs Revenue

---

# 📁 Project Structure

```text
customer-cohort-retention-analysis/
│
├── data/
│   └── Online Retail.xlsx
│
├── output/
│   ├── cleaned_retail_data.csv
│   ├── monthly_business_analysis.csv
│   ├── cohort_customer_counts.csv
│   ├── cohort_retention.csv
│   ├── cohort_retention_heatmap.png
│   ├── customer_metrics.csv
│   ├── rfm_customers.csv
│   │
│   ├── PowerBI_Transactions.csv
│   ├── PowerBI_CustomerMetrics.csv
│   ├── PowerBI_RFMCustomers.csv
│   ├── PowerBI_CohortRetention.csv
│   └── PowerBI_CohortCustomerCounts.csv
│
├── 01_load_and_clean.py
├── 02_eda.py
├── 03_cohort_analysis.py
├── 04_customer_metrics.py
├── 05_rfm_analysis.py
├── 06_export_powerbi.py
│
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-cohort-retention-analysis.git
```

```bash
cd customer-cohort-retention-analysis
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Add the dataset

Download the Online Retail dataset and place:

```text
Online Retail.xlsx
```

inside:

```text
data/
```

The final path should be:

```text
data/Online Retail.xlsx
```

## 4. Run the Python scripts

Run the scripts in the following order:

```bash
python 01_load_and_clean.py
```

```bash
python 02_eda.py
```

```bash
python 03_cohort_analysis.py
```

```bash
python 04_customer_metrics.py
```

```bash
python 05_rfm_analysis.py
```

```bash
python 06_export_powerbi.py
```

---

# 📦 Generated Output Files

The Python pipeline generates:

```text
cleaned_retail_data.csv
monthly_business_analysis.csv
cohort_customer_counts.csv
cohort_retention.csv
cohort_retention_heatmap.png
customer_metrics.csv
rfm_customers.csv
```

Power BI-ready datasets:

```text
PowerBI_Transactions.csv
PowerBI_CustomerMetrics.csv
PowerBI_RFMCustomers.csv
PowerBI_CohortRetention.csv
PowerBI_CohortCustomerCounts.csv
```

---

# 💡 Business Insights

This project can help businesses:

### Improve Customer Retention

Identify customer cohorts with declining retention rates.

### Identify High-Value Customers

Find customers responsible for significant revenue.

### Reduce Customer Churn

Identify customers who are becoming inactive and target them with retention campaigns.

### Improve Customer Loyalty

Understand which customer segments make frequent repeat purchases.

### Optimize Marketing

Create targeted campaigns for:

* Champions
* Loyal Customers
* Potential Loyalists
* At-Risk Customers
* Lost Customers

---

# 🚀 Future Improvements

Future versions of this project can include:

* Predictive customer churn model
* Customer Lifetime Value prediction
* Automated Power BI refresh
* Advanced RFM scoring
* Churn probability prediction
* Personalized marketing recommendations
* SQL database integration
* Automated reporting
* Machine Learning-based customer segmentation

---

# 📚 Key Skills Demonstrated

```text
Python
Pandas
NumPy
Data Cleaning
Exploratory Data Analysis
Customer Analytics
Cohort Analysis
Retention Analysis
RFM Analysis
Customer Segmentation
Power BI
DAX
Data Visualization
Business Intelligence
Business Analysis
Data Storytelling
```

---

# 👨‍💻 Author

**Likith Yadav**

**B.Tech — Computer Science & Engineering**
The Apollo University
**CGPA: 9.5 / 10**

### Technical Skills

`Python` · `SQL` · `Power BI` · `Excel` · `Machine Learning` · `Data Analytics`

### Connect

**LinkedIn:**
https://www.linkedin.com/in/likith-yadav-a865a3379

**GitHub:**
https://github.com/likithyadav128-tech

---

## ⭐ Project Highlights

This project demonstrates an end-to-end analytics workflow:

**Raw Data → Cleaning → EDA → Cohort Analysis → Retention Analysis → RFM Segmentation → Power BI → Business Insights**

It is designed as a portfolio project to demonstrate practical **Data Analyst and Business Intelligence skills**.
