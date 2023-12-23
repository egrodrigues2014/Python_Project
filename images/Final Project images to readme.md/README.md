
# FINAL PROJECT: INVESTMENT SIMULATOR
## Video Demo:  https://youtu.be/sb11eBqmWcg
## Description 

This was my final project to complete the CS50 Introduction to Programming with Python.

INVESTMENT SIMULATOR is a python based application where the user provides inputs values for the simulation (e.g: initial and monthly investment, annual profitability expected and the period in years) and the application shows how much money they will have in the period defined.

## Features

- [x]  Get simulation values from the user
- [x]  Output the simulation result on screen
- [x]  Store simulation result data on a .csv file
- [x]  Shows Monthly Profit graph
- [x]  Shows Monthly Interest Amount graph


## Project Explanation

#### 1. Store data simulation values

The user has to provide exactly one command-line argument, the name (or path) of a csv file. To validate this logic, there is the following function:

```python
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
```

To store data in .csv file, it was used a pandas's method called 'to_csv' :

```python
investment.to_csv(r'C:\Users\Elton\Documents\Python_Project\investment.csv')
```


#### 2. Validate inputs variables from user

The user has to provide positive numeric values for all 4 question:

```python
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
```

To handle errors of user's input, there is this 2 functions:

```python
    def get_float_from_input(question) -> float:
        try:
            answer = float(question)
            if answer < 0:
                raise ValueError
            else:
                return answer
        except ValueError:
            sys.exit("Wrong value used! Expected a positive numeric value.")
```

```python
    def get_int_from_input(question) -> int:
        try:
            answer = int(question)
            if answer < 0:
                raise ValueError
            else:
                return answer
        except ValueError:
            sys.exit("Wrong value used! Expected a positive numeric value.")
```

#### 3. Simulation process

Once the user provide all inputs correctly, the following function runs and create a dataframe object using pandas library to store data. 

```python
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
```

#### 4. Results

The user get the simulation summary printed on screen:

```python
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
```

As well as 2 graphics using plotly library. A line graph representing 'Monthly Profit':
```python
    def line_graph(df, x, y, title):
        graphic = px.line(df, x, y, title=title)
        graphic.show()
```

And a scatter graph representing 'Monthly Interest Amount':
```python
    def scatter_graph(df, x, y, title):
        graphic = px.scatter(df, x, y, title=title, hover_data=[df.index])
        graphic.show()
```
## Demo


### Step 1:

Run Project.py and define a output file name to store the simulation data

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/7bf549423fe03a8740ecbafbcc841f9200d9e272/images/Step1.PNG?raw=true)


### Step 2:

Input initial investment value

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/cecb1308b2db05246bee10ea510313d16f2b9b9c/images/Final%20Project%20images%20to%20readme.md/Step2.PNG?raw=true)


### Step 3:

Input monthly investment value

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/cecb1308b2db05246bee10ea510313d16f2b9b9c/images/Final%20Project%20images%20to%20readme.md/Step3.PNG?raw=true)


### Step 4:

Input annual profitability in % above year inflation

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/cecb1308b2db05246bee10ea510313d16f2b9b9c/images/Final%20Project%20images%20to%20readme.md/Step4.PNG?raw=true)


### Step 5:

Input total period (in years) to simulate the investment

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/cecb1308b2db05246bee10ea510313d16f2b9b9c/images/Final%20Project%20images%20to%20readme.md/Step5.PNG?raw=true)


### Outputs:

Investment simulation result summary

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/cecb1308b2db05246bee10ea510313d16f2b9b9c/images/Final%20Project%20images%20to%20readme.md/Step6.PNG?raw=true)

Graph: Investment result over the years

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/dedbeb03fa801e5f21da5b65bd9efa47cfe0503e/images/Final%20Project%20images%20to%20readme.md/Step7.PNG?raw=true)


Csv file is automatically generated

![Alt text](https://github.com/egrodrigues2014/Python_Project/blob/dedbeb03fa801e5f21da5b65bd9efa47cfe0503e/images/Final%20Project%20images%20to%20readme.md/Step8.PNG?raw=true)

## Documentation

- [Pandas](https://pypi.org/project/pandas/)
- [Plotly](https://pypi.org/project/plotly/)


## About CS50’s Introduction to Programming with Python


CS50’s Introduction to Programming with Python is a open course from Havard University, taught by David J. Malan

An introduction to programming using Python. Learn how to read and write code as well as how to test and “debug” it.Learn about functions, arguments, and return values; variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems that make students how to think algorithmically and solve problems efficiently.
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/egrodrigues2014)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/engineer-elton-rodrigues)

