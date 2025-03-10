# import unittest
# from main import fizzbuzz,is_palindrome,is_prime,are_anagrams,convert_temperature,is_valid_password,ShoppingCart


# class BankCustomer(unittest.TestCase):

#     def setUp(self):
#         self.new_cart=BankCustomer() #create new bank customer object

#     def test_add_item(self):
#         self.assertEqual(self.new_cart.add_item("Cake", 10, 0), False) # addinng item with zero quantity
#         self.assertEqual(self.new_cart.add_item("Juice", 5, -3), False) # addinng item with negative quantity
#         self.assertEqual(self.new_cart.add_item("Chips", 3, 2), True) # addinng valid item 

#     def test_remove(self):
#         self.assertEqual(self.new_cart.add_item("Chips", 3, 2), True)
#         self.assertEqual(self.new_cart.remove_item("Chips"),True)  # removing item in the cart
#         self.assertEqual(self.new_cart.remove_item("Bread"),False)  # removing item not in the cart

#     def test_get_total(self):
#         self.assertEqual(self.new_cart.get_total(), 0.0) # calculating the total for empty cart
#         self.new_cart.add_item("Cake", 10, 2)
#         self.new_cart.add_item("Juice", 5, 3)
#         self.assertEqual(self.new_cart.get_total(), 35.0)
        


    

# if __name__== "__main__":
#     unittest.main(verbosity=2)