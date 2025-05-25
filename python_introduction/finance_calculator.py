

def main():
    try:
        # Prompt user for monthly income and expenses, converting inputs to float for precision
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your total monthly expenses: "))

        # Calculate monthly savings
        monthly_savings = monthly_income - monthly_expenses

        # Annual interest rate assumed at 5%
        annual_interest_rate = 0.05

        # Projected savings after one year including interest
        projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

        # Display results with formatted output
        print(f"Your monthly savings are ${monthly_savings:.2f}.")
        print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

    except ValueError:
        print("Invalid input. Please enter numeric values for income and expenses.")

if __name__ == "__main__":
    main()
