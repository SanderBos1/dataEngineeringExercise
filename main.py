from fake_data_runner import TestDataProducer

# columns: 'customer_id', 'customer_name', 'customer_email', 'order_data', 'product_id', 'product_name', 'product_price'
years = ['2018', '2019', '2020']  # List of years
data_size = 1000  # Data size per CSV File
output_folder = "output"  # Define the folder where your csv files will be stored

# Step 2: Fill in these variables for creating data
products = ["magic", "boardgames", "warhammer"]  # List of categories
max_orders_per_customer = 5  # Minimum size per category
min_product_price = 10  # Maximum size per category
max_product_price = 100  # Total size

# step 3: Fill in these variables for data corruption
columns = ['product_price', 'customer_name', 'customer_email']  # List of columns to corrupt
percentage = [0.1, 0.2, 0.2]  # List of percentages to corrupt
values = [-1, '', '']  # List of values to corrupt


# Step 3: Create the data
data_producer = TestDataProducer(years, data_size, output_folder)
data_producer.create_data(products, max_orders_per_customer, min_product_price, max_product_price)
data_producer.corrupt_data(columns, percentage,values)


