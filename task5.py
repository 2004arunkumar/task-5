#Step 1: Import required libraries
import requests
import tkinter as tk
from tkinter import ttk, messagebox

#Step 2: Define functions for fetching exchange rates and converting currency
def get_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']

def convert_currency(amount, rate):
    return amount * rate

#Step 3: Define the CurrencyConverterApp class for GUI
class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('USD Currency Converter')
        self.root.geometry('400x300')
        
        self.rates = get_exchange_rates()
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text='Amount in USD:').grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text='Convert to:').grid(row=1, column=0, padx=10, pady=10)
        self.currency_var = tk.StringVar(self.root)
        self.currency_dropdown = ttk.Combobox(self.root, textvariable=self.currency_var)
        self.currency_dropdown['values'] = list(self.rates.keys())
        self.currency_dropdown.grid(row=1, column=1, padx=10, pady=10)
        
        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert)
        self.convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, text='', font=('Arial', 12))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    def convert(self):
        amount = float(self.amount_entry.get())
        target_currency = self.currency_var.get()
        rate = self.rates[target_currency]
        converted_amount = convert_currency(amount, rate)
        self.result_label.config(text=f'{amount} USD = {converted_amount:.2f} {target_currency}')

# Step 4: Run the application
if __name__ == '__main__':
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
