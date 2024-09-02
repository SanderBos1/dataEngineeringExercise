import pandas as pd
import numpy as np
from fake_data_runner import FakeData, HelperMockData

FAKE_DATA = FakeData()
HELPER_MOCK_DATA = HelperMockData()

def test_mock_name():
    name = FAKE_DATA.mock_name()
    assert type(name) == str

def test_mock_email():
    email = FAKE_DATA.mock_email()
    assert type(email) == str
    assert '@' in email

def test_mock_date():
    start_date = '2020-01-01'
    end_date = '2020-01-10'
    date = FAKE_DATA.mock_date(start_date, end_date)
    assert type(date) == pd.Timestamp
    
def test_set_price():
    low = 10
    high = 100
    price = FAKE_DATA.set_price(low, high)
    assert type(price) == float
    assert low <= price <= high

def test_make_choice_list():
    column = pd.Series([1, 2, 3, 4, 5])
    number = 1
    choice = HELPER_MOCK_DATA.make_choice_list(column, number)
    assert type(choice) == np.int64
    assert choice in column.values

def test_set_wrong_value():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
    column_name = 'A'
    percentage = 0.2
    value = 0
    df = HELPER_MOCK_DATA.set_wrong_value(df, column_name, percentage, value)
    assert df[column_name].isin([value]).sum() == 1

def test_set_product_information():
    products = ["magic", "boardgames", "warhammer"]
    low = 10
    high = 100
    product_information = HELPER_MOCK_DATA.set_product_information(products, low, high)
    assert type(product_information) == list
    assert len(product_information) == 3
    for product in product_information:
        assert type(product['product_id']) == int
        assert type(product['product_name']) == str
        assert type(product['product_price']) == float
        assert low <= product['product_price'] <= high

def test_set_customers():
    number_customers = 10
    customers = HELPER_MOCK_DATA.set_customers(number_customers)
    assert type(customers) == list
    assert len(customers) == number_customers
    assert type(customers[0]) == dict
    assert 'customer_id' in customers[0].keys()
    assert 'name' in customers[0].keys()
    assert 'email' in customers[0].keys()
    


