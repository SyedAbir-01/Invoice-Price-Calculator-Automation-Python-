import csv

TAX_RATE = 0.10  # 10% tax

INPUT_FILE = "products.csv"
OUTPUT_FILE = "invoice.csv"


def calculate_invoice():
    subtotal = 0
    rows = []

    with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            price = float(row["price"])
            quantity = int(row["quantity"])
            total = price * quantity

            subtotal += total

            rows.append([
                row["product"],
                price,
                quantity,
                round(total, 2)
            ])

    tax = round(subtotal * TAX_RATE, 2)
    grand_total = round(subtotal + tax, 2)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Quantity", "Total"])

        for row in rows:
            writer.writerow(row)

        writer.writerow([])
        writer.writerow(["Subtotal", "", "", subtotal])
        writer.writerow(["Tax (10%)", "", "", tax])
        writer.writerow(["Grand Total", "", "", grand_total])

    print("Invoice created:", OUTPUT_FILE)


if __name__ == "__main__":
    calculate_invoice()
