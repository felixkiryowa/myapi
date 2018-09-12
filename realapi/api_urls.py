"""
This module handles view routes

"""
from api import ManageOrders

class GetApiUrls :

    """
    class to define method to define all routes
    
    """
    @staticmethod
    def get_all_urls(APP):
        """function defining all the api routes """
        order_view = ManageOrders.as_view('order_api')
        APP.add_url_rule('/api/v1/order/', defaults={'order_id': None},
                 view_func=order_view, methods=['GET',])
        APP.add_url_rule('/api/v1/order/add', view_func=order_view, methods=['POST',])
        APP.add_url_rule('/api/v1/order/<int:order_id>', view_func=order_view,
                 methods=['GET', 'PUT', 'DELETE'])

