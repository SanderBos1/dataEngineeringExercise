from faker import Faker
from datetime import datetime
import random
import pandas as pd

class fake_demand:

    def __init__(self, number, start_date, end_date, products, cities):
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
        self.products=products
        self.cities = cities
        self.fake = Faker('nl_NL')


    def mock_data(self):
        data = []
        for _ in range(self.number):
            name = self.fake.name()
            fake_email = self.fake.email()
            fake_city = random.choice(self.cities)
            order_date = self.fake.date_between_dates(date_start=self.start_date, date_end =self.end_date)
            product = random.choice(self.products)
            amount = random.sample(range(10, 80), 1)
            row = [f"{name}", f"{fake_email}", f"{fake_city}", f"{order_date}", f"{product}", f"{amount[0]}"]
            data.append(row)
        return data


def main():
    """
        @number: How many times a fake row is created.
        @start_date: The start date of the faked dataset.
        @end_date: The end date of the faked dataset.
        @products: Define the products that are used by the dataset.
        @location: Where the csv file is saved.
        @Cities: Where the order came from.

    """
    number_rows = 3000
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    products = ['orange', 'apple', 'banana', 'pear']
    cities = ['Eindhoven', 'Delft', "Rotterdam", "Den Haag", "Middelburg"]
    location = 'data/mockdataset_2023.csv'

    fake_dataset_creator = fake_demand(number_rows, start_date, end_date, products, cities)
    dataset = fake_dataset_creator.mock_data()
    df = pd.DataFrame(dataset)
    df.to_csv(location)


if __name__ == '__main__':
    main()