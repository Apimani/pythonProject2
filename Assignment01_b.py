import pandas as pd
import pytest


# A normal method
def display():
    print("This is a normal method")


# Test case: Test method for employee data load
def test_employeesDataLoad():
    # Load the source and target CSV files
    df_source = pd.read_csv('employee_source.csv')
    df_target = pd.read_csv('employee_target.csv')

    # Way 1: Using if-else
'''
    if df_source.equals(df_target):
        print("Matching")
    else:
        print("Differences found")
        pytest.fail("Source and target don't match")

'''
    # Way 2: Using pytest assertion
assert df_source.equals(df_target), "Source and target don't match"
