import csv

filename = input("Enter CSV file path: ").strip()

try:
    file = open(filename, "r")
except FileNotFoundError:
    print("File not found!")
    exit()

reader = csv.DictReader(file)

total = 0
total_quantity = 0

product_revenue = {}

for sale in reader:
    product = sale["product"]

    try:
        price = int(sale["price"])
        quantity = int(sale["quantity"])
    except ValueError:
        print(f"Invalid data for {product}")
        continue

    total_quantity = total_quantity + quantity

    revenue = price * quantity
    total = total + revenue

    if product in product_revenue:
        product_revenue[product] = product_revenue[product] + revenue
    else:
        product_revenue[product] = revenue

file.close()


best_product = ""
best_revenue = 0

for product in product_revenue:
    revenue = product_revenue[product]

    if revenue > best_revenue:
        best_revenue = revenue
        best_product = product


report = f"""
===== SALES REPORT =====

Total revenue: {total:,}
Products sold: {total_quantity}

Product performance:
"""

for product in product_revenue:
    report = report + f"- {product}: {product_revenue[product]:,}\n"

report = report + f"""
Best product: {best_product}
Best revenue: {best_revenue:,}
"""


print(report)


output_filename = "sales_report.txt"

file = open(output_filename, "w")
file.write(report)
file.close()

print(f"Report saved to {output_filename}")
