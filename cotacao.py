import requests

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

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the response data as JSON
    data = response.json()

    # Access the desired information from the response
    rates = data['conversion_rates']

    # Prompt the user for the amount in dollars to convert
    amount_usd = float(input("Enter the amount in USD: "))

    # Perform the conversion for each currency in moedas
    for currency in moedas:
        if currency in rates:
            rate = rates[currency]
            converted_amount = amount_usd * rate
            formatted_amount = formato[currency].format(converted_amount)
            print(f'{moedas[currency]}: {formatted_amount}')

else:
    # Print an error message if the request failed
    print('Failed to retrieve exchange rates')
    