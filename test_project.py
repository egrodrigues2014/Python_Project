from Project import get_float_from_input, get_int_from_input, populate_df
import pytest
import pandas as pd
import datatest as dt


def test_get_float_from_input():
    # Test string values
    with pytest.raises(SystemExit):
        get_float_from_input("cat")

    # Test negative values
    with pytest.raises(SystemExit):
        get_float_from_input("-1")

    # Test zero value
    assert get_float_from_input('0') == 0

    # Test positive values
    assert get_float_from_input('1') == 1


def test_get_int_from_input():
    # Test string values
    with pytest.raises(SystemExit):
        get_int_from_input("cat")

    # Test negative values
    with pytest.raises(SystemExit):
        get_int_from_input("-1")

    # Test zero value
    assert get_int_from_input('0') == 0

    # Test positive values
    assert get_int_from_input('1') == 1


# Check the csv file generated
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    # Considering as input to df: months = 1 , initial_investiment = 1000, monthly_investment = 100 , month interest = 1%
    populate_df(1, 1000, 100, 0.01).to_csv(r'C:\Users\Elton\Documents\Python_Project\investment.csv')
    print(populate_df(1, 1000, 100, 0.01))
    return pd.read_csv('investment.csv')


@pytest.mark.mandatory
def test_columns_name(df):
    dt.validate(
        df.columns,
        {'Month', 'Opening_Balance', 'Monthly_Investment', 'Total_Month_Investment_Amount', 'Interest_Amount',
         'Final_Amount'},
    )


def test_columns_type(df):
    # Expression to accessor syntax in pandas
    dt.register_accessors()

    # Check all columns types
    df['Month'].validate(int)
    df['Opening_Balance'].validate(float)
    df['Monthly_Investment'].validate(float)
    df['Total_Month_Investment_Amount'].validate(float)
    df['Interest_Amount'].validate(float)
    df['Final_Amount'].validate(float)


def test_validate_row_values(df):
    # Expression to accessor syntax in pandas
    dt.register_accessors()

    df['Month'].validate(int)
    df['Opening_Balance'].validate(1000)
    df['Monthly_Investment'].validate(100)
    df['Total_Month_Investment_Amount'].validate(1100)
    df['Interest_Amount'].validate(11)
    df['Final_Amount'].validate(1111)
