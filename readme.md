# Product dataset generator

This python script is written to be used as a random dataset generator for learning data engineering projects.
It generates a dataset with the columns defined below. Keep in mind that some columns intentionally have mistakes.
This is done for learning purposes.

## The dataset

- customerId: The Id of a customer. Issue: does not have to be unique
- customerName: The name of the customer
- customerEmail: The email of the customer. Issue: can have special characters
- orderDate:  The date for which a product is ordered 
- productId: The id of the product that is ordered
- productName: The name of the ordered product. Issue: Can be Nan, which indicates a mistake
- productCategory: The category of the ordered product
- productPrice : The price of the ordered product. Issue: can be -1, which indicates a mistake

