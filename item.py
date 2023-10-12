"""
This is the item class for any Item for Sale
Currently an item will have: 
- Name (The actual name of the item for sale)
- Item Number (Some unique value for searching like OEM, Barcode or Model Number, some items may have some of these or all, so perhaps its best to have a value for each)
- Price (the sale price of the item, some adjustments may be needed to attribute for items with different unit pricing )
- Active (if the item is availble for actual sale or not )
- Stock (the number of units of the actual item itself)
The items should actually pull themselves from an SQLite database, but that is still in progress
TODO: Implement SQLite Database into the relevant methods 
"""
class Item:
    def __init__(self,name,item_number,price,active,stock):
        self.name = name
        self.item_number = item_number
        self.price = price
        self.active = active
        self.stock = stock 

    """
    Core function of an Item is being sold
    We take the total stock being sold and subtract that from the current stock
    Stock should currently not go into the negative but the function for handling the entire sale should validate that. This function is just for tracking stock
    TODO: Add validation to some part of the Selling Process
    TODO: Find better name for this function to indicate that it alters stock and 
    TODO: Look into ways to maybe merge sell_items() and return_items()
    """
    def sell_item(self,sold_stock)
        self.stock = self.stock - sold_stock

    """
    An item being sold may end up being returned 
    We take the total stock being returned and add back to the current stock
    This function needs an added security of checking the existing transaction to make sure the number is within the bounds of the stock sold. 
    TODO: Return to this function once Sale Tracking is Implemented 
    """
    def return_items(self, returned_stock)
        self.stock = self.stock + returned_stock