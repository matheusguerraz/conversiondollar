import requests
import tkinter as tk
from tkinter import ttk

# Defined API key
access_key = '32b8030dba6ccf8b5cf117d5'

# Where USD is the base currency you want to use
url = f'https://v6.exchangerate-api.com/v6/{access_key}/latest/USD'

# Making our request
response = requests.get(url)

moedas = {
    'USD': 'Dólar Americano (USD)',
    'EUR': 'Euro (EUR)',
    'JPY': 'Iene Japonês (JPY)',
    'GBP': 'Libra Esterlina (GBP)',
    'BRL': 'Real (BRL)',
    'AED': 'Dirham dos Emirados Árabes Unidos (AED)',
}

formato = {
    'USD': '$ {:,.2f}',
    'EUR': '€ {:,.2f}',
    'JPY': '¥ {:,.0f}',
    'GBP': '£ {:,.2f}',
    'BRL': 'R$ {:,.2f}',
    'AED': 'AED {:,.2f}',
}

def convert_currency():
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the response data as JSON
        data = response.json()

        # Access the desired information from the response
        rates = data['conversion_rates']

        # Get the selected currency
        selected_currency = currency_var.get()

        # Prompt the user for the amount to convert
        amount = float(amount_entry.get())

        if selected_currency in rates:
            rate = rates[selected_currency]
            converted_amount = amount * rate
            formatted_amount = formato[selected_currency].format(converted_amount)
            result_label.config(text=f'{moedas[selected_currency]}: {formatted_amount}')
        else:
            result_label.config(text='Currency not found')
    else:
        result_label.config(text='Failed to retrieve exchange rates')

# Create the window
window = tk.Tk()
window.title('Currency Converter')
window.geometry('400x300')

# Create the style for the widgets
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), anchor='center')
style.configure('TButton', font=('Arial', 12))

# Create the widgets
amount_label = ttk.Label(window, text='Amount in USD:')
amount_entry = ttk.Entry(window, font=('Arial', 12))
currency_label = ttk.Label(window, text='Select currency:')
currency_var = tk.StringVar(window)
currency_dropdown = ttk.Combobox(window, textvariable=currency_var, values=list(moedas.keys()), font=('Arial', 12))
convert_button = ttk.Button(window, text='Convert', command=convert_currency)
result_label = ttk.Label(window, text='Result will be shown here', font=('Arial', 12))

# Arrange the widgets in the window
amount_label.pack(pady=10)
amount_entry.pack(pady=5)
currency_label.pack(pady=10)
currency_dropdown.pack(pady=5)
convert_button.pack(pady=10)
result_label.pack(pady=10)

# Start the main loop
window.mainloop()
