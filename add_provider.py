import csv

# --- Bikes data for TopGear Bike Rentals ---
bike_data_topgear = {
    "Honda Activa": 500,
    "Honda Activa 6G": 800,
    "Classic 350": 1500,
    "Avenger 220": 1200,
    "Yamaha FZ V1.0": 800,
    "Honda Hornet": 1000,
    "Yamaha FZ V 2.0": 1000,
    "Honda Activa 5G": 600,
    "TVS Ntorq 110": 500
}

# --- Provider name ---
provider = "TopGear Bike Rentals"

# --- Target CSV file ---
csv_file = "bikes_data.csv"

# --- Append data ---
with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for name, price in bike_data_topgear.items():
        writer.writerow([name, f"₹{price}", provider])
        print(f"✅ Appended: {name} - ₹{price} - {provider}")

print(f"\n✅ All TopGear Bike Rentals entries successfully added to '{csv_file}'")
