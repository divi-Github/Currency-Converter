'''
                                        [Currency Converter {CC}]
                                    Programming language used --> Python  
'''
import tkinter as tk
import requests
from tkinter import filedialog, messagebox

def currency_converter():
    try:
        amount = float(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid Input [Please enter a numeric value only]")
        return
    primary_currency = base_currency_var.get()
    secondary_currency = target_currency_var.get()

    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{primary_currency}")
    data = response.json()

    conversion_rate = data['rates'][secondary_currency]
    converted_amount = amount * conversion_rate

    result_label.config(text=str(converted_amount))

window = tk.Tk()
window.title("Currency Converter")
window.geometry("800x400")  
window.resizable(True,True)

l1 = tk.Label(window, text="Enter Amount: ")
l1.pack()

entry = tk.Entry(window)
entry.pack()

l2 = tk.Label(window, text="Primary Currency :")
l2.pack()

countries = [
    "USD",  # United States Dollar
    "EUR",  # Euro
    "GBP",  # British Pound Sterling
    "INR",  # Indian Rupee
    "JPY",  # Japanese Yen
    "CHF",  # Swiss Franc
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CNY",  # Chinese Yuan (Renminbi)
    "NZD",  # New Zealand Dollar
    "BRL",  # Brazilian Real
    "SGD",  # Singapore Dollar
    "ZAR",  # South African Rand
    "SEK",  # Swedish Krona
    "AED",  # United Arab Emirates Dirham
    "RUB",  # Russian Ruble
    "TRY",  # Turkish Lira
    "MXN",  # Mexican Peso
    "KRW",  # South Korean Won
    "NOK",  # Norwegian Krone
    "PLN",  # Polish Złoty
    "HKD",  # Hong Kong Dollar
    "DKK",  # Danish Krone
    "THB",  # Thai Baht
    "ARS",  # Argentine Peso
    "EGP",  # Egyptian Pound
    "MYR",  # Malaysian Ringgit
    "ILS",  # Israeli New Shekel
    "CZK",  # Czech Koruna
]
base_currency_var = tk.StringVar(window)
base_currency_var.set("USD")  # Default Primary currency
base_currency_dropdown = tk.OptionMenu(window, base_currency_var, *countries)
base_currency_dropdown.pack()

l3 = tk.Label(window, text="Secondary Currency :")
l3.pack()

target_currency_var = tk.StringVar(window)
target_currency_var.set("INR")  # Default Secondary currency

target_currency_dropdown = tk.OptionMenu(window, target_currency_var, *countries)
target_currency_dropdown.pack()

label = tk.Label(window, text =   ''' "USD" United States Dollar | "EUR" Euro | "GBP" British Pound Sterling
| "INR" Indian Rupee | "JPY" Japanese Yen | "CHF" Swiss Franc | "AUD" Australian Dollar | "CAD" Canadian Dollar
| "CNY" Chinese Yuan (Renminbi) | "NZD" New Zealand Dollar | "BRL" Brazilian Real | "SGD" Singapore Dollar
| "ZAR" South African Rand | "SEK" Swedish Krona | "AED" United Arab Emirates Dirham | "RUB" Russian Ruble
| "TRY" Turkish Lira | "MXN" Mexican Peso | "KRW" South Korean Won | "NOK" Norwegian Krone | "PLN" Polish Złoty
| "HKD" Hong Kong Dollar | "DKK" Danish Krone | "THB" Thai Baht | "ARS" Argentine Peso |"EGP" Egyptian Pound
| "MYR" Malaysian Ringgit | "ILS" Israeli New Shekel | "CZK" Czech Koruna''',font=("Helvetica",10))
label.pack(padx=20,pady=20)

button = tk.Button(window, text="Convert", command=currency_converter)
button.pack()

l4 = tk.Label(window, text="Amount after conversion :  ")
l4.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

'''********************END OF THE CODE********************'''
