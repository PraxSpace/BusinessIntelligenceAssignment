import csv
import pandas as pd
import numpy as np
from random import randint, choice
from datetime import datetime, timedelta
np.random.seed(42)

# Products data
def createProductCSV(fileName):
    product_data = {
        "Product_ID": [101, 102, 103, 104, 105],
        "Product_Name": ["Salmon", "Soused Herring", "Red Berry Compote", "Vanilla Quark", "Fish Burger"],
        "Category": ["Fish", "Fish", "Dessert", "Dessert", "Fast Food"],
        "Price": [15.00, 10.00, 5.00, 4.50, 8.00],
    }
    df = pd.DataFrame(product_data)
    df.to_csv(fileName, index=False)
    print("File Created Successfully!")
createProductCSV("Product.csv")
product = pd.read_csv("Product.csv")

# Branch data
def createBranchCSV(fileName):
    product_data = {
        "Branch_ID": [1, 2, 3, 4],
        "Branch_Name": ["Flensburg", "Bad Honnef", "Munich", "Hamburg"],
        "City": ["Flensburg", "Bad Honnef", "Munich", "Hamburg"],
        "State": ["Schleswig-Holstein", "North Rhine-Westphalia", "Bavaria", "Hamburg"],
        "Region": ["North", "West", "South", "North"],
    }
    df = pd.DataFrame(product_data)
    df.to_csv(fileName, index=False)
    print("File Created Successfully!")
createBranchCSV("Branch.csv")
branch = pd.read_csv("Branch.csv") 

# Generate sales data   
def createSalesCSV(fileName, branchData, productData):
    sale_id = 1
    start_date = datetime.strptime("2025-08-01", "%Y-%m-%d")
    num_days = 180  # Number of days of sales
    Sale_ID_data = []
    Date_data = []
    Time_Data = []
    Branch_ID_Data = []
    Product_ID_Data = []
    Qty_Data = []
    Amount_Data = []
    for day_offset in range(num_days):
        current_date = start_date + timedelta(days=day_offset)
        for _ in range(randint(3, 7)):  # Random 3-7 sales per day
            Sale_ID_data.append(sale_id)
            sale_id += 1
            time_hour = randint(10, 20)
            time_minute = choice([0, 15, 30, 45])
            sale_time = f"{time_hour:02d}:{time_minute:02d}"
            Date_data.append(current_date.strftime("%Y-%m-%d"))
            Time_Data.append(sale_time)
            Branch_ID_Data.append(choice(branchData["Branch_ID"]))
            prodID = choice(productData["Product_ID"])
            Product_ID_Data.append(prodID)
            qty = randint(1, 10)
            Qty_Data.append(qty)
            prodPrice = productData.loc[productData['Product_ID'] == prodID, 'Price'].values[0]
            Amount_Data.append(round(qty * prodPrice , 2))
            
    data = {
        "Sale_ID": Sale_ID_data,
        "Date": Date_data,
        "Time": Time_Data,
        "Branch": Branch_ID_Data,
        "Product": Product_ID_Data,
        "Qty": Qty_Data,
        "Amount": Amount_Data,
    }
    df = pd.DataFrame(data)
    df.to_csv(fileName, index=False)
    print("File Created Successfully!")
createSalesCSV("Sales.csv", branch, product)





