salesData = {}

with open("icecream.txt", "r") as data:
    # Initialize total sales for each store
    total_sales_stores = {}
    for line in data:
        if ":" in line:
            parts = line.strip().split(":")
            flavor = parts[0]
            sales = [float(part) for part in parts[1:]]
            total_sales = sum(sales)
            salesData[flavor] = {'sales': sales, 'total_sales': total_sales}
    print(salesData)