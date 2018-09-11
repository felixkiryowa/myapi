from unittest import TestCase
from api import ManageOrders

class Tests(TestCase) :
    def setUp(self):
          #creating an object of class calculator
        self.order  = ManageOrders()

    def test_get_orders(self):
         """
        Test case for get orders endpoint, it gets all orders
        """
