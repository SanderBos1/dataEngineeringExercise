from faker import Faker
from datetime import datetime
import random
import pandas as pd

class fake_demand:

    def __init__(self, number, start_date, end_date, products):
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
        self.products=products
        self.fake = Faker('nl_NL')


    def mock_data(self):
        data = []
        for _ in range(self.number):
            name = self.fake.name()
            fake_address = self.fake.address()
            fake_email = self.fake.email()
            order_date = self.fake.date_between_dates(date_start=self.start_date, date_end =self.end_date)
            product = random.choice(self.products)
            amount = random.sample(range(10, 80), 1)
            row = [name, fake_address, fake_email, order_date, product, amount[0]]
            data.append(row)
        return data


def main():
    """
        @number: how many times a fake row is created
        @start_date: The start date of the faked dataset
        $end_date: The end date of the faked dataset
    """
    number = 100
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    products = ['orange', 'apple', 'banana', 'pear']
    location = 'data/mockdataset.csv'

    fake_dataset_creator = fake_demand(number, start_date, end_date, products)
    dataset = fake_dataset_creator.mock_data()
    df = pd.DataFrame(dataset)
    df.to_csv(location)
    print(df)



main()