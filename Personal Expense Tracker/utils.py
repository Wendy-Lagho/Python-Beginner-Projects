
def validate_amount(amount):
    try:
        return float(amount)
    except ValueError:
        raise ValueError("Invalid amount. Please enter a valid number.")
