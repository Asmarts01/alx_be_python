monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
# Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print (monthly_savings, "is your monthly savings.")
print (projected_savings, "is your projected savings at the end of the year.")