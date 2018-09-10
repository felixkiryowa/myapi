"""This is orders class defining the class constructor """

class Orders(object):
    """This is orders class"""

    def __init__(self, order_id, item_name, quantity, price):
        """This is orders class constructor"""
        self.order_id = order_id
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
