import unittest
from main import BankCustomer


class TestBankCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 =BankCustomer("Reema","Radi","pass1234") 
        self.customer2 =BankCustomer("reema","Radi","r01222") 
        self.customer3 =BankCustomer("Shouq","Radi","Sh@@ouq1") 
        # self.customer4 =BankCustomer("233","59","sara0909") 
    def test_add_new_customer(self):
        self.assertEqual(self.customer1.add_new_customer(), False) # if customer aleady exists
        self.assertEqual(self.customer2.add_new_customer(), False) # if the customer already exists (case insensitive)
        self.assertEqual(self.customer3.add_new_customer(), True) # if the customer doesn't exists
        # self.assertEqual(self.customer4.add_new_customer(),False)
        
    
class TestWithdraw(unittest.TestCase):    
    def setUp(self):
        self.customer5 =BankCustomer("Reema","Radi","pass1234") 
        self.customer5.balance_checking=1500
        self.customer5.balance_savings=1000
        
    def test_withdraw_from_checking_account(self):
        self.assertEqual(self.customer5.withdraw_from_checking_account(500), True) # successful withdraw
        self.assertEqual(self.customer5.withdraw_from_checking_account(1100), False) # invalid withdraw, insufficient balance
        self.assertEqual(self.customer5.withdraw_from_checking_account(-300), False) # invalid withdraw amount (negative)
        self.assertEqual(self.customer5.withdraw_from_checking_account(0), False) # invalid withdraw amount (zero)
        self.assertEqual(self.customer5.withdraw_from_checking_account(150), False) # withdraw without login
        
        
    def test_withdraw_from_savings_account(self):
        
        self.assertEqual(self.customer5.withdraw_from_savings_account(500), True) # successful withdraw
        self.assertEqual(self.customer5.withdraw_from_savings_account(600), False) # invalid withdraw, insufficient balance
        self.assertEqual(self.customer5.withdraw_from_savings_account(-30), False) # invalid withdraw amount (negative)
        self.assertEqual(self.customer5.withdraw_from_checking_account(0), False) # invalid withdraw amount (zero)
        self.assertEqual(self.customer5.withdraw_from_savings_account(100), False) # withdraw without login

class TestDeposit(unittest.TestCase):  
    def setUp(self):
        self.customer6 =BankCustomer("Reema","Radi","pass1234") 
        self.customer6.balance_checking=1000
        self.customer6.balance_savings=1000 
        
    def test_deposit_to_checking_account(self):
        self.assertEqual(self.customer6.deposit_to_checking_account(500), True) # successful deposit
        self.assertEqual(self.customer6.deposit_to_checking_account(-200), False) # invalid deposit amount (negative)
        self.assertEqual(self.customer6.deposit_to_checking_account(0), False) # invalid deposit amount (zero)
        self.assertEqual(self.customer6.deposit_to_checking_account(50), False) # deposit without login
    
        
    def test_deposit_to_savings_account(self):
        self.assertEqual(self.customer6.deposit_to_savings_account(500), True) # successful deposit
        self.assertEqual(self.customer6.deposit_to_savings_account(-200), False) # invalid deposit amount (negative)
        self.assertEqual(self.customer6.deposit_to_savings_account(0), False) # invalid deposit amount (zero)
        self.assertEqual(self.customer6.deposit_to_savings_account(50), False) # deposit without login
    

    



if __name__== "__main__":
    unittest.main(verbosity=2)