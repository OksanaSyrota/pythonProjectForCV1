import unittest
from POM.page_object.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class LoginPageTestSuits(unittest.TestCase):

    customerName = "Ron Weasly"


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Chrome()
        cls.wait = WebDriverWait(cls.driver, 60)
        cls.login_page = LoginPage(cls.driver, cls.wait)

    def test_open_customer_account_page(self):
        # Login Page
        self.login_page.go_to_customer_login_page()
        self.login_page.click_customer_login_button()
        # Select Name Page
        self.assertEqual("Your Name :", self.login_page.get_your_name_text())
        self.assertEqual(['---Your Name---', 'Hermoine Granger', 'Harry Potter', 'Ron Weasly', 'Albus Dumbledore',
                          'Neville Longbottom'],
                         [item.text for item in Select(self.login_page.check_customer_name_list()).options])
        self.login_page.select_name_from_list()
        self.login_page.click_login_button()
        # Account Page Assert
        self.assertEqual("Ron Weasly", self.login_page.get_welcome_name_text())

    def test_opened_account_page(self):
        # Account Page
        self.login_page.select_number_of_currency()
        self.assertEqual(['1007', '1008', '1009'],
                         [item.text for item in Select(self.login_page.check_currency_number_list()).options])
        self.assertEqual('Dollar', self.login_page.check_correct_name_of_currency())
        # Deposit Form
        self.login_page.click_deposit_button()
        self.login_page.enter_amount_for_deposit()
        self.login_page.click_deposit_submit_button()
        self.assertEqual('Deposit Successful', self.login_page.get_successful_text())
        # WithDrawl Form
        self.login_page.click_withdrawl_button()
        self.login_page.enter_amount_for_withdrawl()
        self.login_page.click_withdrawl_submit_button()
        self.assertEqual('Transaction successful', self.login_page.get_successful_text_for_withdrawl())
        # Transaction Form
        self.login_page.click_transaction_button()
        #self.assertEqual([['test', '100', 'credit']], self.login_page.transactions_table()) DATA!!!!!

        # Return To Home Page
        self.login_page.click_home_button()
        self.login_page.click_bank_manager_login_button()
        # Add Customer Form
        self.login_page.click_add_customer_button()
        self.login_page.enter_first_name()
        self.login_page.enter_last_name()
        self.login_page.enter_postal_code()
        self.login_page.click_add_customer_submit_form()
        self.login_page.switch_to_alert()
        self.assertEqual('Customer added successfully with customer id :6', self.login_page.switch_to_alert())
        self.login_page.accept_alert()
        # Open Account Page
        self.login_page.click_open_account_button()
        self.login_page.select_created_account_from_drop_down()
        self.login_page.select_currency_for_created_account()
        self.login_page.click_process_button()
        self.assertEqual('Account created successfully with account Number :1016',
                         self.login_page.switch_to_account_number_alert())
        self.login_page.accept_account_number_alert()
        # Customers Page
        self.login_page.click_customers_button()
        self.assertEqual([['Hermoine', 'Granger', 'E859AB', '1001 1002 1003', 'Delete'],
                          ['Harry', 'Potter', 'E725JB', '1004 1005 1006', 'Delete'],
                          ['Ron', 'Weasly', 'E55555', '1007 1008 1009', 'Delete'],
                          ['Albus', 'Dumbledore', 'E55656', '1010 1011 1012', 'Delete'],
                          ['Neville', 'Longbottom', 'E89898', '1013 1014 1015', 'Delete'],
                          ['Oksana', 'Yakymets', '79000', '1016', 'Delete']], self.login_page.customers_table())
        self.login_page.enter_created_customer_in_search_field()
        self.assertEqual([['Oksana', 'Yakymets', '79000', '1016', 'Delete']], self.login_page.search_results_page())
        self.login_page.delete_created_customer()
        self.assertEqual([], self.login_page.search_results_page_after_deleted_account())


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()