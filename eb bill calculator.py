def calculate_eb_bill(units):
    """
    Function to calculate electricity bill based on slab rates.
    Adjust slab rates and fixed charges as per your EB rules.
    """

    bill_amount = 0

    # Example slab rates (replace with your local EB tariff)
    if units <= 100:
        bill_amount = units * 1.5   # ₹1.5 per unit
    elif units <= 200:
        bill_amount = (100 * 1.5) + (units - 100) * 2.0
    elif units <= 500:
        bill_amount = (100 * 1.5) + (100 * 2.0) + (units - 200) * 3.0
    else:
        bill_amount = (100 * 1.5) + (100 * 2.0) + (300 * 3.0) + (units - 500) * 5.0

    # Add fixed charges (example: ₹50)
    fixed_charge = 50
    total_bill = bill_amount + fixed_charge

    return total_bill


# Example usage
units_consumed = int(input("Enter units consumed: "))
bill = calculate_eb_bill(units_consumed)
print(f"Total Electricity Bill: ₹{bill:.2f}")
print("thankyou")