from faker import Faker
from datetime import datetime
import random
import pandas as pd

class fake_demand:

    def __init__(self, number, years, products, cities):
        self.number = number
        self.years = years
        self.products=products
        self.cities = cities
        self.fake = Faker('nl_NL')


    def mock_data(self):
        data = []
        for year in self.years:
            start_date = datetime(year, 1, 1)
            end_date = datetime(year, 12, 31)
            location = f'data/mockdataset_{year}.csv'
            for _ in range(self.number):
                name = self.fake.name()
                fake_email = self.fake.email()
                fake_city = random.choice(self.cities)
                order_date = self.fake.date_between_dates(date_start=start_date, date_end =end_date)
                product = random.choice(self.products)
                amount = random.randint(-1, 100)
                row = [f"{name}", f"{fake_email}", f"{fake_city}", f"{order_date}", f"{product}", f"{amount}"]
                data.append(row)
            df = pd.DataFrame(data)
            df.to_csv(location)


def main():
    """
        @number: How many times a fake row is created.
        @years: a list of years, for each year a dataset is created.
        @products: Define the products that are used by the dataset.
        @location: Where the csv file is saved.
        @Cities: Where the order came from.

    """
    number_rows = 3000
    years = [2021, 2022,2023]
    products = ['orange', 'apple', 'banana', 'pear']
    cities = ['Eindhoven', 'Delft', "Rotterdam", "Den Haag", "Middelburg"]

    fake_dataset_creator = fake_demand(number_rows, years, products, cities)
    fake_dataset_creator.mock_data()



if __name__ == '__main__':
    main()