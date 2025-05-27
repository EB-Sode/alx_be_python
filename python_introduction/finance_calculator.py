monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses

annual_interest= (monthly_savings) *12*0.05
total_monthly_savings = monthly_savings*12

annual_savings = total_monthly_savings + annual_interest

print(f"Your monthly savings are: ${monthly_savings}")
print("Projected savings after one year, with interest, is: "f"${annual_savings}") 
