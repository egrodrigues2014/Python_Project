import sys
import pandas as pd
import plotly.express as px

def main():

    # Step 1
    # Check if the output file is correct
    check_command_line_ags()



    # Step 2
    # Get input values from user

    # Initial Investiment
    initial_investment = float(input("What is your initial investiment in USD? \n"))

    # Monthly investment
    monthly_investment = float(input("What will be your monthly investiment in USD? \n"))

    # Profitability
    year_prof = float(input("What annual profitability(%) will you consider above inflation? \n"))
    month_prof = (year_prof/12)/100

    # Period in years
    period_in_years = int(input("How many years do you want to leave your money invested? \n"))
    period_in_months = period_in_years * 12




    # Step 3
    # Create and populate dataframe


    # Amount = C*(1+i)^n
    # C = Capital invested
    # i = interest
    # n = period

    # Create data frame in pandas
    investment = pd.DataFrame()

    # Create loop in period range
    for m in range(1,period_in_months+1):

        if m == 1:
            # Opening balance for m == 1 : it is the initial investment
            opening_balance = initial_investment
        else:
            # For m > 1, we get the final ammount of the last month as month opening balanc
            opening_balance = investment.loc[m-1, 'Final_Amount']

        # Total investiment of the month will be opening_balance + monthly_investment
        month_inv_ammount = opening_balance + monthly_investment

        # Period interest ammount
        interest = month_inv_ammount * month_prof

        # Final month amount = Total investiment of the month + interest
        final_month_amount = month_inv_ammount + interest

        # Insert data in the investment dataframe
        investment.loc[m, 'Opening_Balance'] = round(opening_balance, 2)
        investment.loc[m, 'Monthly_Investment'] = round(monthly_investment, 2)
        investment.loc[m, 'Total_Month_Investment_Amount'] = round(month_inv_ammount, 2)
        investment.loc[m, 'Interest_Amount'] = round(interest, 2)
        investment.loc[m, 'Final_Amount'] = round(final_month_amount, 2)
        investment.index.name = 'Month'

    # Step 4
    # Send data to a file
    # investment.to_excel(r'C:\Users\Elton\Documents\Python_Project\investment.xlsx')
    investment.to_csv(r'C:\Users\Elton\Documents\Python_Project\investment.csv')


    # Step 5
    # Results

    # Get last final month amount
    final_amount = investment.iloc[-1,-1]


    # Total invested
    total_invested = investment['Monthly_Investment'].sum() + initial_investment


    # Interest earned
    total_interest_earned = final_amount - total_invested


    # Profitability
    profitability = total_interest_earned / total_invested

    # Print results

    print("====================================================================================================================================")
    print(f"In {period_in_years} year(s) you will have ${final_amount:,.2f}")
    print(f"Total invested : ${total_invested:,.2f}")
    print(f"Taking into account an annual interest of {(year_prof/100):.2%}, you will earn ${total_interest_earned:,.2f} of interest amount.")
    print(f"It means that {(total_interest_earned/final_amount):.02%} of all you will have came from interests.")
    print(f"Finally, you earned {profitability:.02%} of all you invested! ")
    print("====================================================================================================================================")

    # Step 6
    # Graphics

    # Line graphic
    graphic = px.line(investment, investment.index, 'Final_Amount', title='Monthly Profit')
    graphic.show()

    # Scatter graphic
    graphic = px.scatter(investment,'Final_Amount','Interest_Amount',title='Monthly Interest Amount', hover_data=[investment.index])
    graphic.show()

def function_1():
    ...


def function_2():
    ...


def check_command_line_ags():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print(f"{sys.argv[1]} is not a CSV file")
        sys.exit(1)


if __name__ == "__main__":
    main()