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


    def mock_data_products(self):
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

    def mock_data_cities(self):
        city_data = []
        for city in self.cities:
            monthly_capacity = random.randint(800, 1200)
            order_rates = []
            for product in self.products:
                order_rate = random.randint(10, 50)
                order_rate_product = f"{product} throughput rate is {order_rate}"
                order_rates.append(order_rate_product)
            cost = random.randint(100, 700)
            row = [f"{city}", f"{cost}", f"{monthly_capacity}", f"{order_rates}"]
            city_data.append(row)
        location = f'data/mockdataset_cities.csv'
        df = pd.DataFrame(city_data)
        df.to_csv(location)


def main():
    """
        @number: How many times a fake row is created.
        @years: a list of years, for each year a dataset is created.
        @products: Define the products that are used by the dataset.
        @Cities: Where the order came from.

    """
    number_rows = 3000
    years = [2021, 2022,2023]
    products = ['orange', 'apple', 'banana', 'pear']
    cities = ['Eindhoven', 'Delft', "Rotterdam", "Den Haag", "Middelburg"]

    fake_dataset_creator = fake_demand(number_rows, years, products, cities)
    fake_dataset_creator.mock_data_products()
    fake_dataset_creator.mock_data_cities()



if __name__ == '__main__':
    main()