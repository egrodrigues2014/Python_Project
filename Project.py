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
    question1 = input("What is your initial investiment in USD? \n")
    initial_investment = get_float_from_input(question1)

    # Monthly investment
    question2 = input("What will be your monthly investiment in USD? \n")
    monthly_investment = get_float_from_input(question2)

    # Profitability
    question3 = input("What annual profitability(%) will you consider above inflation? \n")
    year_prof = get_float_from_input(question3)
    month_prof = (year_prof / 12) / 100

    # Period in years
    question4 = input("How many years do you want to leave your money invested? \n")
    period_in_years = get_int_from_input(question4)
    period_in_months = period_in_years * 12
    if period_in_months == 0:
        sys.exit("No period defined for the simulation")


    # Step 3
    # Create and populate dataframe
    investment = populate_df(period_in_months , initial_investment, monthly_investment, month_prof)
    # print(investment)

    # Step 4
    # Send data to a csv file
    investment.to_csv(r'investment.csv')


    # Step 5
    # Calculate Results

    # Get last final month amount
    final_amount = investment.iloc[-1, -1]

    # Total invested
    total_invested = investment['Monthly_Investment'].sum() + initial_investment
    if total_invested == 0:
        sys.exit("Total invested for this simulation is zero.")

    # Interest earned
    total_interest_earned = final_amount - total_invested

    # Profitability
    profitability = total_interest_earned / total_invested


    # Print results
    print(
        "====================================================================================================================================")
    print(f"In {period_in_years} year(s) you will have ${final_amount:,.2f}")
    print(f"Total invested : ${total_invested:,.2f}")
    print(
        f"Taking into account an annual interest of {(year_prof / 100):.2%}, you will earn ${total_interest_earned:,.2f} of interest amount.")
    print(f"It means that {(total_interest_earned / final_amount):.02%} of all you will have came from interests.")
    print(f"Finally, you earned {profitability:.02%} of all you invested! ")
    print(
        "====================================================================================================================================")


    # Step 6
    # Graphics

    # Line graphic
    line_graph(investment, investment.index, 'Final_Amount', 'Monthly Profit')
    print("Openning Monthly Profit graph ... ")

    # Scatter graphic
    scatter_graph(investment, 'Final_Amount', 'Interest_Amount', 'Monthly Interest Amount')
    print("Openning Monthly Interest Amount graph ... ")


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


def get_float_from_input(question) -> float:
    try:
        answer = float(question)
        if answer < 0:
            raise ValueError
        else:
            return answer
    except ValueError:
        sys.exit("Wrong value used! Expected a positive numeric value.")


def get_int_from_input(question) -> int:
    try:
        answer = int(question)
        if answer < 0:
            raise ValueError
        else:
            return answer
    except ValueError:
        sys.exit("Wrong value used! Expected a positive numeric value.")


def populate_df(months : int, init_inv : float, monthly_inv : float, m_prof : float) -> pd.DataFrame:
    # Amount = C*(1+i)^n
    # C = Capital invested
    # i = interest
    # n = period

    # Create data frame in pandas
    df = pd.DataFrame()
    # Create loop in period range
    for m in range(1, months + 1):

        if m == 1:
            # Opening balance for m == 1 : it is the initial investment
            opening_balance = init_inv
        else:
            # For m > 1, we get the final ammount of the last month as month opening balance
            try:
                opening_balance = df.loc[m - 1, 'Final_Amount']
            except:
                sys.exit("There is no profitability in this simulation")

        # Total investiment of the month will be opening_balance + monthly_investment
        month_inv_ammount = opening_balance + monthly_inv

        # Period interest ammount
        interest = month_inv_ammount * m_prof

        # Final month amount = Total investiment of the month + interest
        final_month_amount = month_inv_ammount + interest

        # Insert data in the investment dataframe
        df.loc[m, 'Opening_Balance'] = round(opening_balance, 2)
        df.loc[m, 'Monthly_Investment'] = round(monthly_inv, 2)
        df.loc[m, 'Total_Month_Investment_Amount'] = round(month_inv_ammount, 2)
        df.loc[m, 'Interest_Amount'] = round(interest, 2)
        df.loc[m, 'Final_Amount'] = round(final_month_amount, 2)
        df.index.name = 'Month'

    # Return dataframe
    return df


def line_graph(df, x, y, title):
    graphic = px.line(df, x, y, title=title)
    graphic.show()


def scatter_graph(df, x, y, title):
    graphic = px.scatter(df, x, y, title=title, hover_data=[df.index])
    graphic.show()


if __name__ == "__main__":
    main()
