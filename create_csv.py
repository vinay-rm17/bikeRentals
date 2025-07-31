import csv

# File name
csv_file = "bikes_data.csv"

# Create the CSV file with headers
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Bike Name", "Price (₹)", "Provider"])  # Header row

print(f"✅ {csv_file} created with headers.")
