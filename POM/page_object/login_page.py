import time

from POM.page_object.base_object import BaseObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


locators = {
    # Login Page
    "customerLoginButton": (By.CSS_SELECTOR, "[ng-click='customer()']"),
    "bankManagerLoginButton": (By.CSS_SELECTOR, "[ng-click='manager()']"),
    # Select Name Page
    "yourNameText": (By.CSS_SELECTOR, "div > label"),
    "userSelectDropDownList": (By.CSS_SELECTOR, "#userSelect"),
    "loginButton": (By.CSS_SELECTOR, "[type='submit']"),
    # Account Page
    "logoutButton": (By.CSS_SELECTOR, ".logout"),
    "welcomeCustomerNameText": (By.CSS_SELECTOR, ".fontBig"),
    "currencySelectDropDownList": (By.CSS_SELECTOR, "#accountSelect"),
    "selectedCurrency": (By.CSS_SELECTOR, ".center .ng-binding:nth-child(3)"),
    "transactionsButton": (By.CSS_SELECTOR, "[ng-click='transactions()']"),
    "depositButton": (By.CSS_SELECTOR, "[ng-click='deposit()']"),
    "withdrawlButton": (By.CSS_SELECTOR, "[ng-click='withdrawl()']"),
    "amountField": (By.CSS_SELECTOR, "[ng-model='amount']"),
    "SubmitButton": (By.CSS_SELECTOR, "[type='submit']"),
    "DepositSuccessfulText": (By.CSS_SELECTOR, ".error"),
    "amountFieldWithdrawl": (By.CSS_SELECTOR, "[ng-model='amount']"),
    "SubmitButtonWithdrawl": (By.CSS_SELECTOR, "[type='submit']"),
    "DepositSuccessfulTextWithdrowl": (By.CSS_SELECTOR, ".error"),
    "backButton": (By.CSS_SELECTOR, "[ng-click='back()']"),
    # Table For Transactions
    "tableRows": (By.CSS_SELECTOR, "tbody > tr"),
    "cell": (By.CSS_SELECTOR, "td"),
    # Home
    "homeButton": (By.CSS_SELECTOR, ".home"),
    # Bank Account Page
    "addCustomerButton": (By.CSS_SELECTOR, "[ng-click='addCust()']"),
    "openAccountButton": (By.CSS_SELECTOR, "[ng-click='openAccount()']"),
    "CustomersButton": (By.CSS_SELECTOR, "[ng-click='showCust()']"),
    # Add Customer Form
    "firstNameField": (By.CSS_SELECTOR, "[ng-model='fName']"),
    "lastNameField": (By.CSS_SELECTOR, "[ng-model='lName']"),
    "postCodeField": (By.CSS_SELECTOR, "[ng-model='postCd']"),
    "addCustomerButtonForSubmitForm": (By.CSS_SELECTOR, "[type='submit']"),
    # Open Account Page
    "processButton": (By.CSS_SELECTOR, "[type='submit']"),
    "customerNameSelectDropDownList": (By.CSS_SELECTOR, "#userSelect"),
    "currencyDropDownListForOpenAccount": (By.CSS_SELECTOR, "#currency"),

    # Customers Page
    "searchField": (By.CSS_SELECTOR, "[ng-model='searchCustomer']"),
    "deleteCustomerButton": (By.CSS_SELECTOR, "[ng-click='deleteCust(cust)']"),
    "tableRowsForCustomers": (By.CSS_SELECTOR, "tbody > tr"),
    "cellForCustomersTable": (By.CSS_SELECTOR, "td"),




}


class LoginPage(BaseObject):

    def go_to_customer_login_page(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        self.wait.until(EC.visibility_of_element_located(locators["customerLoginButton"]))

    def click_customer_login_button(self):
        self.driver.find_element(*locators["customerLoginButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["userSelectDropDownList"]))

    def get_your_name_text(self):
        return self.driver.find_element(*locators["yourNameText"]).text

    def check_customer_name_list(self):
        return self.driver.find_element(*locators["userSelectDropDownList"])

    def select_name_from_list(self):
        Select(self.driver.find_element(*locators["userSelectDropDownList"])).select_by_visible_text("Ron Weasly")
        self.wait.until(EC.element_to_be_clickable(locators["loginButton"]))

    def click_login_button(self):
        self.driver.find_element(*locators["loginButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["logoutButton"]))

    def get_welcome_name_text(self):
        return self.driver.find_element(*locators["welcomeCustomerNameText"]).text

    def select_number_of_currency(self):
        self.wait.until(EC.visibility_of_element_located(locators["currencySelectDropDownList"]))
        Select(self.driver.find_element(*locators["currencySelectDropDownList"])).select_by_visible_text("1007")

    def check_currency_number_list(self):
        return self.driver.find_element(*locators["currencySelectDropDownList"])

    def check_correct_name_of_currency(self):
        return self.driver.find_element(*locators["selectedCurrency"]).text

    def click_deposit_button(self):
        self.driver.find_element(*locators["depositButton"]).click()
        self.wait.until(EC.element_to_be_clickable(locators["amountField"]))

    def enter_amount_for_deposit(self):
        self.driver.find_element(*locators["amountField"]).send_keys('100')

    def click_deposit_submit_button(self):
        self.driver.find_element(*locators["SubmitButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["DepositSuccessfulText"]))

    def get_successful_text(self):
        return self.driver.find_element(*locators["DepositSuccessfulText"]).text

    ###
    def click_withdrawl_button(self):
        self.driver.find_element(*locators["withdrawlButton"]).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(locators["amountFieldWithdrawl"]))

    def enter_amount_for_withdrawl(self):
        self.driver.find_element(*locators["amountFieldWithdrawl"]).send_keys('50')

    def click_withdrawl_submit_button(self):
        self.driver.find_element(*locators["SubmitButtonWithdrawl"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["DepositSuccessfulTextWithdrowl"]))

    def get_successful_text_for_withdrawl(self):
        return self.driver.find_element(*locators["DepositSuccessfulTextWithdrowl"]).text
    ###
    # Transaction Form

    def click_transaction_button(self):
        self.driver.find_element(*locators["transactionsButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["backButton"]))

    # Test Table For Transactions
    def transactions_table(self):
        tableData = []
        for row in self.driver.find_elements(*locators["tableRows"]):
            rowData = []
            for cell in row.find_elements(*locators["cell"]):
                rowData.append(cell.text)
            tableData.append(rowData)
        return tableData

    # Return To Home Page
    def click_home_button(self):
        self.driver.find_element(*locators["homeButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["bankManagerLoginButton"]))

    def click_bank_manager_login_button(self):
        self.driver.find_element(*locators["bankManagerLoginButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["addCustomerButton"]))

    # Bank Account Page
    def click_add_customer_button(self):
        self.driver.find_element(*locators["addCustomerButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["addCustomerButtonForSubmitForm"]))

    def enter_first_name(self):
        self.driver.find_element(*locators["firstNameField"]).send_keys('Oksana')

    def enter_last_name(self):
        self.driver.find_element(*locators["lastNameField"]).send_keys('Yakymets')

    def enter_postal_code(self):
        self.driver.find_element(*locators["postCodeField"]).send_keys('79000')

    def click_add_customer_submit_form(self):
        self.driver.find_element(*locators["addCustomerButtonForSubmitForm"]).click()
        self.wait.until(EC.alert_is_present())

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
        self.wait.until(EC.visibility_of_element_located(locators["openAccountButton"]))

    # Open Account Page
    def click_open_account_button(self):
        self.driver.find_element(*locators["openAccountButton"]).click()
        self.wait.until(EC.element_to_be_clickable(locators["customerNameSelectDropDownList"]))

    def select_created_account_from_drop_down(self):
        Select(self.driver.find_element(*locators["customerNameSelectDropDownList"])).select_by_value("6")

    def select_currency_for_created_account(self):
        Select(self.driver.find_element(*locators["currencyDropDownListForOpenAccount"])).select_by_visible_text("Dollar")

    def click_process_button(self):
        self.driver.find_element(*locators["processButton"]).click()

    def switch_to_account_number_alert(self):
        return self.driver.switch_to.alert.text

    def accept_account_number_alert(self):
        self.driver.switch_to.alert.accept()

    # Customers Page
    def click_customers_button(self):
        self.driver.find_element(*locators["CustomersButton"]).click()
        self.wait.until(EC.visibility_of_element_located(locators["searchField"]))

    def customers_table(self):
        customersTable = []
        for row in self.driver.find_elements(*locators["tableRowsForCustomers"]):
            rowCustomers = []
            for cell in row.find_elements(*locators["cellForCustomersTable"]):
                rowCustomers.append(cell.text)
            customersTable.append(rowCustomers)
        return customersTable

    def enter_created_customer_in_search_field(self):
        self.driver.find_element(*locators["searchField"]).send_keys("Yakymets")
        self.wait.until(EC.visibility_of_element_located(locators["deleteCustomerButton"]))

    def search_results_page(self):
        searchResultsTable = []
        for row in self.driver.find_elements(*locators["tableRowsForCustomers"]):
            rowCustomers = []
            for cell in row.find_elements(*locators["cellForCustomersTable"]):
                rowCustomers.append(cell.text)
            searchResultsTable.append(rowCustomers)
        return searchResultsTable

    def delete_created_customer(self):
        self.driver.find_element(*locators["deleteCustomerButton"]).click()

    def search_results_page_after_deleted_account(self):
        searchResultsTable = []
        for row in self.driver.find_elements(*locators["tableRowsForCustomers"]):
            rowCustomers = []
            for cell in row.find_elements(*locators["cellForCustomersTable"]):
                rowCustomers.append(cell.text)
            searchResultsTable.append(rowCustomers)
        return searchResultsTable

