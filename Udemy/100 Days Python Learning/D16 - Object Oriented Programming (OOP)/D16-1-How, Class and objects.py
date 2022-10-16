"""Re-modelling a real world situation into a programming words by Splitting a larger task into smaller pieces and
chunking it """

"""Example simulations: Having Restaurant
0. You
    Managing all these manpower to do what are they set to do
1. The receptionist
    To handle the reservations, preparing a seat, and manage the guests
2. The waitress
    To pickup the order, deliver into cooking teams, and deliver it into the guest
3. The Chef
    Cooking the guest's order, maintain the cooking materials
4. The Cleaner
    Cleaning everything after the guest is leaving"""

"""Translating into a programming words
translating it by:
1. The Role => Class
    - what they have  => attributes
    - what they do  => methods
"""
#2. The waiter
class Waiter:
    # what they have
    is_holding_plate = True
    order_tables = [4, 5, 6]

    #what they do
    def take_order(table,order):
    #takes order to the chef
        pass

def take_payment(amount):
    #add money to restaurant
    pass

