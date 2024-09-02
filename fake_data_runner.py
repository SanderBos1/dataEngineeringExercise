import os
import random
from faker import Faker
import pandas as pd
import numpy as np

class FakeData:
    def __init__(self):
        self.faker = Faker()

    def mock_name(self):
        return self.faker.name()

    def mock_email(self):
        return self.faker.email(safe=False)

    def mock_date(self, start_date, end_date):
        helper_mock_data = HelperMockData()
        date_range = pd.date_range(start=start_date, end=end_date)
        data = helper_mock_data.make_choice_list(date_range, 1)
        return data

    def set_price(self, low, high):
        price = random.uniform(low, high)
        return price


class HelperMockData():
    def __init__(self):
        pass

    def make_choice_list(self, column:pd.Series, number=1, weights=None):
        choice = random.choices(column, k=number, weights=weights)
        if number == 1:
            return choice[0]
        return choice

    def set_wrong_value(self, df: pd.DataFrame, column_name: str, percentage: float, value: str) \
         -> pd.DataFrame:
        if percentage < 0 or percentage > 1:
            raise ValueError("Percentage must be between 0 and 1")

        column = df[column_name]
        number_to_replace = int(len(column) * percentage)
        indices = np.random.choice(len(column), size=number_to_replace, replace=False)
        df.loc[indices, column_name] = value

        return df

    def set_product_information(self, products, low, high):
        product_information = []
        length = len(products)
        data_faker = FakeData()
        for i in range(length):
            product = {
                'product_id': i+1,
                'product_name': products[i],
                'product_price': data_faker.set_price(low, high)
            }
            product_information.append(product)
        return product_information

    def set_customers(self, number_customers):
        data_faker = FakeData()
        customers = []
        for i in range(number_customers):
            customer = {
                'customer_id': i+1,
                'name': data_faker.mock_name(),
                'email': data_faker.mock_email()
            }
            customers.append(customer)
        return customers

class TestDataProducer:

    def __init__(self, years, rows, location):
        self.year_amount = years
        self.rows = rows
        self.location = location

    def create_data(self, product_names, max_orders, low_price, high_price):
        fake_data = FakeData()
        helper_mock_data = HelperMockData()

        product_information = helper_mock_data.set_product_information(product_names, \
                                                                       low_price, high_price)
        customers = helper_mock_data.set_customers(100)

        for year in self.year_amount:
            data = []
            for _ in range(self.rows):
                customer = helper_mock_data.make_choice_list(customers)
                customer_id = customer['customer_id']
                name = customer['name']
                email = customer['email']
                orders_per_customer = random.randint(1, max_orders)
                for _ in range(orders_per_customer):
                    date = fake_data.mock_date(f'{year}-01-01', f'{year}-12-31')
                    chosen_product = helper_mock_data.make_choice_list(product_information)
                    product_id = chosen_product['product_id']
                    product_name = chosen_product['product_name']
                    product_price = chosen_product['product_price']
                    data.append([customer_id, name, email, date, product_id, product_name, \
                                 product_price])
            save_location = f"{self.location}/{year}_clean.csv"
            self.save_data(data, save_location)

    def corrupt_data(self, column_list, percentage_list,  value_list):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        save_directory = os.path.join(base_dir, self.location)

        file_list = os.listdir(save_directory)
        for file in file_list:
            if not file.endswith(".csv"):
                continue
            year = file.split("_")[0]
            df = pd.read_csv(f"{save_directory}/{file}")
            helper_mock_data = HelperMockData()
            for item_number in range(len(column_list)):
                df = helper_mock_data.set_wrong_value(df, column_list[item_number], \
                        percentage_list[item_number], value_list[item_number])
            location = f"output/{year}_corrupted.csv"
            self.save_data(df, location)

    def save_data(self, data, location):
        df = pd.DataFrame(data, columns=['customer_id', 'customer_name', 'customer_email', \
                                'order_data', 'product_id', 'product_name', 'product_price'])
        df = df.sort_values('order_data')
        df.to_csv(location, index=False)
