from wage_engine import calculate_wage

sample_data = {
    "payment_model": "hourly",
    "hours_worked": 80,
    "hourly_rate": 125,
    "deliveries": 0,
    "rate_per_delivery": 0,
    "expected_bonus": 2500,
    "agreed_deductions": 500,
    "actual_payment": 9500
}

result = calculate_wage(sample_data)

print("WAGEWISE AI - TEST RESULT")
print("-------------------------")

for key, value in result.items():
    print(f"{key}: {value}")