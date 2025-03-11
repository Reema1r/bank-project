import unittest
from main import BankCustomer 
from main import Account

# ************ This test works fine ************
class TestBankCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 =BankCustomer("Reema","Radi","pass1234",0,0) 
        self.customer2 =BankCustomer("reema","Radi","r01222",0,0) 
        self.customer3 =BankCustomer("Shouq","Radi","Sh@@ouq1",0,0) 
                
    def test_add_new_customer(self): 
        self.assertEqual(self.customer1.add_new_customer(), False) # if customer aleady exists
        self.assertEqual(self.customer2.add_new_customer(), False) # if the customer already exists (case insensitive)
        self.assertEqual(self.customer3.add_new_customer(), True) # if the customer doesn't exists
    
    
    
# ************ This test works fine ************
class TestWithdraw(unittest.TestCase):    
    def setUp(self):
        self.customer5 =Account("10009","pass1234") 
        self.customer5.balance_checking=1500
        self.customer5.balance_savings=-30
        
    def test_withdraw_from_account(self):
        self.assertEqual(self.customer5.perform_withdraw(-30,"checking"), False) # unsuccessful withdraw (negative withdraw amount)
        self.assertEqual(self.customer5.perform_withdraw(0, "savings"), False) # unsuccessful withdraw (zero withdraw amount)

        # Test if the account balance > 0
        self.assertEqual(self.customer5.perform_withdraw(500,"checking"), True) # successful withdraw
        self.assertEqual(self.customer5.perform_withdraw(4000,"checking"), False) # unsuccessful withdraw (insufficient account balance)
        
        # Test if the account balance <0
        self.assertEqual(self.customer5.perform_withdraw(150,"savings"), False) # unsuccessful withdraw (negative balance and trying to withdraw more than 100$)
        self.assertEqual(self.customer5.perform_withdraw(80, "savings"), False) # unsuccessful withdraw (negative balance and withdraw amount is les than 100$ but will result in account balance less than 100$ )
        



if __name__== "__main__":
    unittest.main(verbosity=2)