import tkinter as tk


from openpyxl import load_workbook, Workbook
from datetime import datetime

def save_to_excel():
    date = date_entry.get()
    description = description_entry.get()
    category = category_entry.get()
    payment_mode = payment_mode_entry.get()
    entry_type = entry_type_entry.get()
    amount = amount_entry.get()
    month = month_entry.get()
    year = year_entry.get()

    filename = "Prashanth - Expense Tracker (1).xlsx"
    wb = None

    try:
        try:
            wb = load_workbook(filename)
        except FileNotFoundError:
            wb = Workbook()
            sheet = wb.active
            headers = ["Date", "Description", "Category", "Payment mode", "Type", "Amount", "Month", "Year", "Month - Year"]
            sheet.append(headers)

        sheet = wb.active
        row_data = [date, description, category, payment_mode, entry_type, amount, month, year, f"{month}-{year}"]
        sheet.append(row_data)

        wb.save(filename)
        status_label.config(text=f"Data saved to {filename}")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
    finally:
        if wb:
            wb.close()

root = tk.Tk()
root.minsize(400,400)
root.title("Expense Tracker Form")


# Create label
l = tk.Label(root, text="Expense Tracker 2.0")
l.config(font=("Courier", 14))

l.pack()


date_label = tk.Label(root, text="Date:")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

description_label = tk.Label(root, text="Description:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

category_label = tk.Label(root, text="Category:")
category_label.pack()
category_entry = tk.Entry(root)
category_entry.pack()

payment_mode_label = tk.Label(root, text="Payment Mode:")
payment_mode_label.pack()
payment_mode_entry = tk.Entry(root)
payment_mode_entry.pack()

entry_type_label = tk.Label(root, text="Type:")
entry_type_label.pack()
entry_type_entry = tk.Entry(root)
entry_type_entry.pack()

amount_label = tk.Label(root, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

month_label = tk.Label(root, text="Month:")
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

year_label = tk.Label(root, text="Year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

save_button = tk.Button(root, text="Save to Excel", command=save_to_excel)
save_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()


root.mainloop()