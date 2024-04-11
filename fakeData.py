from faker import Faker
from datetime import datetime
import random
import pandas as pd

class fakeDemand:

    def __init__(self, number, years, products, productCategories):
        self.number = number
        self.years = years
        self.products=products
        self.productCategories = productCategories
        self.fake = Faker('nl_NL')


    def mockDataDirty(self):
        data = []
        for year in self.years:
            startDate = datetime(year, 1, 1)
            endDate = datetime(year, 12, 31)
            location = f'data/mockProductData_{year}.csv'
            for _ in range(self.number):
                customerId = self.fake.random_int(min=1, max=self.number)
                customerName = self.fake.name()
                customerEmail = self.fake.email(safe=False)
                orderDate = self.fake.date_between_dates(date_start=startDate, date_end =endDate)
                productCategory = random.choice(self.productCategories)
                pickedProduct = random.choice(self.products[productCategory])
                productName = random.choices([ "NaN", pickedProduct[0]], weights = [1 , 10])[0]
                productId = pickedProduct[1]
                productPrice = random.choices([-1, pickedProduct[2]] , weights =[2, 10])[0]
                row = [customerId, customerName, customerEmail, orderDate,productId,  productName, productCategory, productPrice]
                data.append(row)

            df = pd.DataFrame(data)
            df.to_csv(location, index=False)

    def mockDataClean(self):
        data = []
        for year in self.years:
            startDate = datetime(year, 1, 1)
            endDate = datetime(year, 12, 31)
            location = f'data/mockProductDataClean_{year}.csv'
            for i in range(self.number):
                customerId = i
                customerName = self.fake.name()
                customerEmail = self.fake.email(safe=False)
                orderDate = self.fake.date_between_dates(date_start=startDate, date_end =endDate)
                productCategory = random.choice(self.productCategories)
                pickedProduct = random.choice(self.products[productCategory])
                productName = pickedProduct[0]
                productId = pickedProduct[1]
                productPrice = pickedProduct[2]
                row = [customerId, customerName, customerEmail, orderDate,productId,  productName, productCategory, productPrice]
                data.append(row)

            df = pd.DataFrame(data)
            df.to_csv(location, index=False)



def main(cleanData = False):
    """ 
        @cleanData: boolean that determines if the data is clean or not
        @number: How many times a fake row is created.
        @years: a list of years, for each year a dataset is created.
        @products: Define the product that are used by the dataset.
        @productCategories: Define the product categories that are used by the dataset.

    """
    numberRows = 3000
    years = [2021, 2022,2023]
    productCategories = ["cardGames", "boardGames", "videoGames", "minatureGames"]
    products = {
        "cardGames": [["magicTheGathering", 1, random.randint(40, 80)], ["explodingKittens", 2, random.randint(40, 80)]],
        "boardGames": [["settlersOfCatan", 3, random.randint(40, 80)], ["monopoly", 4, random.randint(40, 80)], ["wingSpan", 5, random.randint(40, 80)]],
        "videoGames": [["eu4", 6, random.randint(40, 80)], ["civ5", 7, random.randint(40, 80)], ["ageOfEmpires", 8, random.randint(40, 80)]],
        "minatureGames": [["warhammer40k", 9, random.randint(40, 80)], ["warmachine", 10, random.randint(40, 80)]]

    }

    fake_dataset_creator = fakeDemand(numberRows, years, products, productCategories)

    if cleanData == False:
        fake_dataset_creator.mockDataDirty()
    else:
        fake_dataset_creator.mockDataClean()




if __name__ == '__main__':
    main()