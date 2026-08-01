import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Ecommerce_Sales_Project.xlsx")

#! phase one data exploration 
print(df)
print(df.shape)
df.info()
# df info is enough
print(df.describe())
print(df.columns)
print(df.head(10))
# in this phase we explore the dataset given to and check its information with 
# different functions

#! phase two finding Problem in the dataset 
print(df.isnull())
# it check the missing value and return true or false
print(df.isnull().sum())
#it check the misssing value give the sum of missing values in each column
print(df.isnull().sum().sum())
# the above function gives total missing values

print(df.duplicated())
# it helps us to find duplicate values in the data
print(df.duplicated().sum())
# it count all the duplicate values 
df.drop_duplicates(inplace=True)
# it removes the all duplicate values and inplace = true means it change the original data
print(df.shape)
# it change the og data beacuse of inplace and shape chack the shape 
print("Duplicate rows removed successfully.")
print(type(df))
df["Discount_%"] = df["Discount_%"].fillna(0)
# it fill the discount's missing values with zero from previous operation we known that 
# city and dicount has two none value we fill them with fillana
df["City"] = df["City"].fillna("Unknown")
print("filling successfull")
# we fill the missing value using  fillna function  

#! phase three date analysis
# task one 
# ? creating the new column revenew which is Revenue = Quantity × Price
df["Revenue"] = df["Quantity"] * df["Price"]
# this line create the revenue by multiplying the quantity and price 
print("Revenue column is added successfully")


# task two 
#? calculating total revenue
total_revenue = df["Revenue"].sum()

print(f"Total Revenue: ₹{total_revenue:,.2f}")
#here f is for clean string printing and 2f for show s the two digit after decimal point
# here we add the all  revenue values
# this gives us the total sum of revenue 

# task 3 
#? Most Sold Product

product_quantity  = df.groupby("Product")["Quantity"].sum()
print(product_quantity)
# this crete a group of product and then sum their quantity 
print("Highest selling product :",product_quantity.idxmax())
# it give us the product that sold most 
print("quantity sold :",product_quantity.max())
#it gives us the price of that product 
# this tells us the which product sold most 
 
 # task 4
 #?Revenue by Category

category_revenue = df.groupby("Category")["Revenue"].sum()

print(category_revenue)
# this single statement gives us the revenue of every category

# task 5 
#? Revenue be cities 

city_revenue = df.groupby("City")["Revenue"].sum()
print(city_revenue)
# this statement gives us the city with their revenue 
print(city_revenue.sort_values(ascending=False).head(5))
# this is sort the value according to ascending order and give top 5 values 


#!Phase 4: Business Insights
#?Task 1: Most Preferred Payment Method
count_payments = df["Payment_Method"].value_counts()
#this function help us to count the values in the certain dataset
print(count_payments)
print("most use payment method:",count_payments.idxmax())
print("How many times use :",count_payments.max())
# above two statement s show us that how many times and which method use 

#?Task 2: Order Status Report
order_status = df["Status"].value_counts()
#it work very good but do not forget s it's counts not count
print(order_status)

# ?Task 3: City with Maximum Orders
city_orders = df["City"].value_counts()
print(city_orders)
print(city_orders.idxmax())
print(city_orders.max())
# OR
# city_orders = df.groupby("City").size()

#?Task 4: Average Discount by Category
average_discount_by_category = df.groupby("Category")["Discount_%"].mean()
print(average_discount_by_category)
# the above statement provide the avarege discount by category which include all category and 
#their avarege dicount 

#?Task 5: Revenue After Discount
df["Final_Revenue"] = df["Revenue"] - (df["Revenue"] * df["Discount_%"] / 100)
print(df.head())
print("final revenue column is added succssfully ")

#!Phase 5: Advanced Business Analysis
#? Task 1: Top 10 Customers by Spending
top_10_customer = df.groupby("Customer")["Final_Revenue"].sum()
print(top_10_customer.sort_values(ascending=False).head(10))
# this gives us the top 10 customer with the highest spendings 
#here we take values from the customer s according to their final revenue and then sum all values
# then sort values ascending = false to ascending order of values and the head 10 for top 10 values

#?Task 2: Monthly Revenue Analysis
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# this statement convert the order date into the actul date and time 
months = df["Order_Date"].dt.month_name()
# it gives us the actul months name
Revenue_by_months = df.groupby(months)["Final_Revenue"].sum()
print("Total final revenue for each month",Revenue_by_months)

#?Task 3: Best Sales Month
print("The month with the highest Revenue:",Revenue_by_months.idxmax())
print("Revenue of that month:",Revenue_by_months.max())

#?Task 4: Category-wise Sales Report
# df.groupby("Category")["Quantity"].sum()
# df.groupby("Category")["Revenue"].sum()
# df.groupby("Category")["Discount_%"].mean()
#we can combine above statements with agg function

category_analysis = df.groupby("Category").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Average_Discount=("Discount_%", "mean")
)
# in this we use groupby and the agg to combine the statement 
# we also rename them by total quantity and other two 
# otherwise we can simply use 
# category_analysis = df.groupby("Category").agg({
#     "Quantity": "sum",
#     "Revenue": "sum",
#     "Discount_%": "mean"
# })

# print(category_analysis)
# this give same output but without rename

print(category_analysis)

category_analysis.to_excel("Project_Report.xlsx", index=False)
print("successful")

# this is for matplotlib practice
x = Revenue_by_months.index
y = Revenue_by_months.values
plt.plot(x,y)
plt.show()
# # ============================================
# Pandas Series + Matplotlib Rule
# ============================================
# A Pandas Series always has:
#
# Index  -> Labels (Usually X-axis)
# Values -> Numbers (Usually Y-axis)
#
# Examples:
#
# city_revenue
# Mumbai     50000
# Pune       42000
# Nagpur     31000
#
# x = city_revenue.index
# y = city_revenue.values
#
# plt.plot(x, y)
#
# This same logic works for:
# ✔ Monthly Revenue
# ✔ Category Revenue
# ✔ Top Customers
# ✔ Product Sales
# ✔ City Sales
# ============================================











