# Product dataset generator

This python script is written to be used as a random dataset generator.
It generates two datasets which are defined below

## product dataset
The product dataset simulate the sales of different products of a fictional company.
It has the following columns

- name: The name of a customer
- email: The email of a customer
- city: The city where the order was placed
- order_date: The date for which the order was placed
- product: Which product was sold
- amount: How many of each product where sold, -1 indicates a mistake in the data

## city dataset

The city dataset simulate the cost of the warehouses, its throughput capacity and it storage capacity. 
It has the following columns:

- city: the name of the city
- monthly_capacity: How much of each product can be stored
- order_rate: How many items of each product can be made per hour
- cost: the cost of the location 