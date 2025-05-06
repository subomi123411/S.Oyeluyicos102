import pandas as pd

# Define the data for Cadbury Nigeria Plc's products and brands
data = {
    "Segment": ["Refreshment Beverages", "Confectionery", "Intermediate Cocoa Products"],
    "Products": [
        "Bournvita, Hot Chocolate",
        "Tom Tom, Buttermint",
        "Cocoa Powder, Cocoa Butter, Cocoa Liquor, Cocoa Cake"
    ],
    "Brands": [
        "CADBURY BOURNVITA, CADBURY 3-in-1 HOT CHOCOLATE",
        "TOMTOM CLASSIC, TOMTOM STRAWBERRY, BUTTERMINT",
        "COCOA POWDER, COCOA BUTTER"
    ]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("cadbury_market.csv")

# Print confirmation message
print("The Cadbury market data has been successfully saved to 'cadbury_market.csv'.")
print(df)