
def calculate_wage(data):

    payment_model = data["payment_model"]

    # Calculate basic earnings
    if payment_model == "hourly":
        base_earnings = (
            float(data.get("hours_worked", 0))
            * float(data.get("hourly_rate", 0))
        )

    elif payment_model == "per_delivery":
        base_earnings = (
            int(data.get("deliveries", 0))
            * float(data.get("rate_per_delivery", 0))
        )

    else:
        raise ValueError("Invalid payment model")

    # Additional earnings and deductions
    bonus = float(data.get("expected_bonus", 0))
    deductions = float(data.get("agreed_deductions", 0))
    actual_payment = float(data["actual_payment"])

    # Calculate expected payment
    expected_gross = base_earnings + bonus
    expected_net = expected_gross - deductions

    # Compare expected and actual payment
    discrepancy = expected_net - actual_payment

    if discrepancy > 0.01:
        status = "Potential Shortfall"

    elif discrepancy < -0.01:
        status = "Payment Above Estimate - Review Inputs"

    else:
        status = "Matches Entered Terms"

    return {
        "base_earnings": round(base_earnings, 2),
        "bonus": round(bonus, 2),
        "deductions": round(deductions, 2),
        "expected_gross": round(expected_gross, 2),
        "expected_net": round(expected_net, 2),
        "actual_payment": round(actual_payment, 2),
        "discrepancy": round(discrepancy, 2),
        "status": status
    }
