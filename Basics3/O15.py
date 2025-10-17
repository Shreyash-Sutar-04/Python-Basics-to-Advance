# Sample sales data: rows = regions, columns = months
sales = [
    [2000, 3000, 2500],
    [1500, 2800, 3200],
    [4000, 5000, 4500]
]

total_sales = 0
for region in sales:          # Outer loop → each region
    for month_sale in region: # Inner loop → each month in that region
        total_sales += month_sale

print(f"Total Sales = {total_sales}")
