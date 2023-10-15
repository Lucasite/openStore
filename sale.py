"""
This is the current Sale Class for a Sale
A Sale is a collection of items being sold to one entity 
Every Sale should have a: 
- Sale No. (some special value to identify any specific transaction)
- Sale Date (the date of the transaction)
- Customer Name (The name of the customer involved in the transaction)
- Sale Inventory (The collection of items being sold)
- Sale Price (the sold price of the goods in the inventory)
"""

class Sale: 
    def __init__(self, sale_no, sale_date,customer_name,goods_sold,sale_price):
        self.sale_no = sale_no
        self.sale_date = sale_date
        self.customer_name = customer_name
        self.goods_sold = goods_sold
        self.sale_price = sale_price

    """
    TODO: Find what core functionality may be required from the Sale Object Specifically,
    beyond simply creating a new sale
    """