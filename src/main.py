from currency_converter import CurrencyConverter


def convert_currency(amount, from_currency, to_currency):
    print(f"Converting {amount} from {from_currency} to {to_currency}")
    c = CurrencyConverter()
    new_amount = c.convert(amount, from_currency, to_currency)
    rounded_amount = round(new_amount, 2)
    print(f"Converted amount: {rounded_amount}")
    return rounded_amount
