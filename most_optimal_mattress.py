import pandas as pd
import numpy as np

def total_ratings():
    df = pd.read_csv('amazon_products.csv')
    df.columns = df.columns.str.strip().str.lower()

    df['ratings'] = df['ratings'].replace('[^\d\.]', '', regex=True).astype(int)
    
    df_sorted = df.sort_values(by=['ratings', 'price'], ascending=[False, True])


    print("\nTop 5 mattresses by total amount of reviews:")
    print(df_sorted.head(5))

    print("\nAverage amount of ratings:", int(round(df['ratings'].mean(), 2)))
    
def price():
    df = pd.read_csv('amazon_products.csv')
    df.columns = df.columns.str.strip().str.lower()
    # Convert price to numeric (remove $ and commas if present)
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Sort by price (ascending = lowest first)
    df_sorted = df.sort_values(by='price', ascending=True)

    print("\nTop 5 mattresses by lowest price:")
    print(df_sorted.head(5))

    print("\nAverage price: $", round(df['price'].mean(), 2))
if __name__ == "__main__":
    type = input("What quality are you looking for in this mattress? (total ratings or price)")
    if type == "total ratings":
        total_ratings()
    elif type == "price":
        price()
    
    

