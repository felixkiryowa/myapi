"""This module defines api views"""
from flask import jsonify
from flask import request
from flask.views import MethodView
from orders import Orders


class ManageOrders(MethodView):
    """Class to define all the api end points"""
    order1 = Orders(1, "pizza", 1, 40000)
    order2 = Orders(2, "pilawoo", 2, 3500)
    order3 = Orders(3, "fresh juice", 3, 30000)

    orders = [order1, order2, order3]

    def get(self, order_id):
        """function to get a single order or to get all the orders"""
        if order_id is None:
            # return a list of orders
            return jsonify({'orders':[order.__dict__ for order in self.orders]})
        specific_order = [
            order.__dict__ for order in self.orders 
            if order.__dict__["order_id"] == order_id
        ]
        return jsonify({'order':specific_order[0]})
    def post(self):
        """funtion to place a new order"""
        # create a new user
        order = Orders(
            request.json['order_id'], request.json['item_name'], 
            request.json['quantity'], request.json['price']
        )
        self.orders.append(order)
        return jsonify({'orders':[order.__dict__ for order in self.orders]})               
    def put(self, order_id):
        """function to update a specific  order"""
        # update a single user
        for order in self.orders:
            if order.__dict__["order_id"] == order_id:
                order_json = request.get_json()
                order.__dict__['item_name'] = order_json['item_name']
                order.__dict__['quantity'] = order_json['quantity']
                order.__dict__['price'] = order_json['price']
        return jsonify({'orders':[order.__dict__ for order in self.orders]})
