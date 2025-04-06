import pandas as pd

# Ensure the 'tabulate' library is installed for markdown output
try:
    import tabulate
except ImportError:
    print("The 'tabulate' library is required for markdown output. Install it using 'pip install tabulate'.")

# Define categories and data for girls and boys
categories = ["Name", "Age", "Height", "Score"]
girls_data = [
    ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"],
    [17, 16, 17, 18, 16, 18, 17, 20, 19, 17],
    [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5],
    [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]
]
boys_data = [
    ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"],
    [19, 16, 18, 17, 20, 19, 16, 18, 17, 19],
    [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7],
    [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]
]

# Combine girls' and boys' data into a single dictionary
data = {category: girls_data[i] + boys_data[i] for i, category in enumerate(categories)}

# Create a DataFrame from the combined data
df = pd.DataFrame(data)

# Display the table in markdown format
print(df.to_markdown(index=False))
