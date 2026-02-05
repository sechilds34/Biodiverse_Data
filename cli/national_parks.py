import os, glob, uuid, hashlib
import json
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from app.queries import queries
from app.db import get_engine

data_amount = {
    #Amount of Rows User Wants to See 
    "1": ("10 Rows", 10),
    "2": ("25 Rows", 25),
    "3": ("50 Rows", 50),
    "4": ("100 Rows", 100),
    "5": ("250 Rows", 250),
    "6": ("500 Rows", 500),
    "7": ("1000 Rows", 1000),
    "8": ("All Rows", None),
}
engine = get_engine()
while True:
    print ("\nAvailable Queries:\n")

    for k, (name, sql) in queries.items():
        print(f"{k}. {name}")

    print("Type 'quit' to exit.")

    choice = input("\nEnter number to run: ").strip().lower()
    #Exit Con
    if choice == "quit":
       print("\n Exiting Analysis Viewing\n")
       break

    ##Error Handle
    if choice not in queries:
        print("Invalid Input")
        continue

    #User chooses amount of rows to view
    print("\nHow Many Rows You'd Like to View\n")
    for key, (label,_) in data_amount.items():
        print(f"{key}. {label}")
    
    row_choice = input("\nChoose Here or 'quit' to Exit: ").strip().lower()
    #Exit Con
    if row_choice == "quit":
        print("\n Exiting Analysis Viewing\n")
        break
    #choice handeling
    if row_choice == "8":
        n = None
    elif row_choice in data_amount:
        n = data_amount[row_choice][1] 
    else:
        print("Invalid Amount, defaulting to 25")
        n = 26

    
    # Run Query
    name, sql = queries[choice]
    print(f"\nRunning: {name}\n")

    #Print Results
    df = pd.read_sql(sql, engine)
    if df.shape == (1, 1):
        print(df.iloc[0, 0])
    else:
        print(df.to_string(index = False) if n is None else df.head(n).to_string(index = False))
    


