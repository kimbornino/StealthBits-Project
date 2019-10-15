import unittest
from selenium import webdriver
import HtmlTestRunner
import time
from StealthBitsPOM.Pages.HomePage import HomePage
from StealthBitsPOM.Pages.Computers import Computers
from StealthBitsPOM.Pages.Users import Users
import selenium.webdriver.support.ui
# import selenium.webdriver.support.ui.expected_conditions as EC

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/kimbo/PycharmProjects/StealthBits/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_home_link(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.go_to_page(home_page.home_button_xpath)
        found_url = driver.current_url
        self.assertEqual(found_url,'https://sb-qawebtest.azurewebsites.net/')

    def test_computers_link(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.go_to_page(home_page.computers_button_xpath)
        found_url = driver.current_url
        self.assertEqual(found_url, 'https://sb-qawebtest.azurewebsites.net/computers')

    def test_users_link(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.go_to_page(home_page.users_button_xpath)
        found_url = driver.current_url
        self.assertEqual(found_url, 'https://sb-qawebtest.azurewebsites.net/computers')

    def test_default_entry_rows(self):
        driver = self.driver
        users = Users(driver)
        self.driver.get('https://sb-qawebtest.azurewebsites.net/users')
        items_count = users.get_row_count()
        self.assertEqual(items_count,10)

    def test_user_entry_rows_25(self):
        driver = self.driver
        self.driver.get('https://sb-qawebtest.azurewebsites.net/users')
        users = Users(driver)
        self.driver.find_element_by_xpath(users.page_display_options_xpath).click()
        self.driver.find_element_by_xpath("//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::li[2]").click()
        items_count = users.get_row_count()
        self.assertEqual(items_count, 25)

    def test_user_entry_rows_100(self):
        driver = self.driver
        self.driver.get('https://sb-qawebtest.azurewebsites.net/users')
        users = Users(driver)
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::div[5]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::li[3]").click()
        items_count = users.get_row_count()
        self.assertEqual(items_count, 100)

    def test_return_to_10(self):
        driver = self.driver
        users = Users(driver)
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::div[5]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::li[2]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::div[5]").click()
        self.driver.find_element_by_xpath("//*[@id='menu-']/div[3]/ul/li[1]").click()
        items_count = users.get_row_count()
        self.assertEqual(items_count, 10)

    def test_menu_bar_exists_on_home(self):
        self.driver.get('https://sb-qawebtest.azurewebsites.net')
        menu_bar = self.driver.find_element_by_class_name('MuiAppBar-positionStatic')
        print(menu_bar)
        self.assertNotEqual(menu_bar, None)

    def test_menu_bar_exists_on_users(self):
        self.driver.get('https://sb-qawebtest.azurewebsites.net/users')
        menu_bar = self.driver.find_element_by_class_name('MuiAppBar-positionStatic')
        print(menu_bar)
        self.assertNotEqual(menu_bar, None)

    def test_menu_bar_exists_on_computers(self):
        self.driver.get('https://sb-qawebtest.azurewebsites.net/computers')
        menu_bar = self.driver.find_element_by_class_name('MuiAppBar-positionStatic')
        print(menu_bar)
        self.assertNotEqual(menu_bar, None)


    def test_check_for_name_heading_on_users(self):
        driver = self.driver
        users = Users(driver)
        text_found = users.get_header(users.header_1)
        self.assertEqual(text_found, 'Name')

    def test_check_for_email_heading_on_users(self):
        driver = self.driver
        users = Users(driver)
        text_found = users.get_header(users.header_2)
        self.assertEqual(text_found, 'Email')

    def test_check_for_Domain_heading_on_users(self):
        driver = self.driver
        users = Users(driver)
        text_found = users.get_header(users.header_3)
        self.assertEqual(text_found, 'Domain')

    def test_check_for_Last_Logon_heading_on_users(self):
        driver = self.driver
        users = Users(driver)
        text_found = users.get_header(users.header_4)
        self.assertEqual(text_found, 'Last Logon')

    def test_check_for_name_heading_on_computers(self):
        driver = self.driver
        computers = Computers(driver)
        text_found = computers.get_header(computers.header_1)
        self.assertEqual(text_found, 'Name')

    def test_check_for_DNS_Host_Name_heading_on_computers(self):
        driver = self.driver
        computers = Computers(driver)
        text_found = computers.get_header(computers.header_2)
        self.assertEqual(text_found, 'DNS Host Name')

    def test_check_for_IP_Address_heading_on_computers(self):
        driver = self.driver
        computers = Computers(driver)
        text_found = computers.get_header(computers.header_3)
        self.assertEqual(text_found, 'IP Address')

    def test_check_for_OS_heading_on_computers(self):
        driver = self.driver
        computers = Computers(driver)
        text_found = computers.get_header(computers.header_4)
        self.assertEqual(text_found, 'OS')

    def test_check_for_OS_Version_heading_on_computers(self):
        driver = self.driver
        computers = Computers(driver)
        text_found = computers.get_header(computers.header_5)
        self.assertEqual(text_found, 'OS Version')

    def test_user_tile_format_correct(self):
        driver = self.driver
        users = Users(driver)
        self.driver.get('https://sb-qawebtest.azurewebsites.net')
        time.sleep(3)
        text = driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::p[4]").text
        tile_number = int(text)
        correctFormat = False
        if tile_number >= 1000:
            if 'K' in text:
                correctFormat = True

        if tile_number < 1000:
            if 'K' not in text:
                coorrectFormat = True
        self.assertEqual(True, correctFormat)

    def test_computer_tile_format_correct(self):
        driver = self.driver
        computers = Users(driver)
        self.driver.get('https://sb-qawebtest.azurewebsites.net')
        time.sleep(3)
        text = driver.find_element_by_xpath(
            "// * [ @ id = 'root'] / div / div[2] / div[1] / div / a / p[2]").text
        tile_number = int(text)
        correctFormat = False
        if tile_number >= 1000:
            if 'K' in text:
                correctFormat = True

        if tile_number < 1000:
            if 'K' not in text:
                correctFormat = True
        self.assertEqual(True, correctFormat)

    def test_computer_tile_number_matches_count(self):
        driver = self.driver
        driver.get('https://sb-qawebtest.azurewebsites.net/computers')
        time.sleep(3)
        pagination_text = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/p[2]").text
        pagination_array = pagination_text.split(" ")
        total_entries = pagination_array[2]
        driver.get('https://sb-qawebtest.azurewebsites.net/')
        time.sleep(3)
        tile_total = driver.find_element_by_xpath(
            "// * [ @ id = 'root'] / div / div[2] / div[1] / div / a / p[2]").text
        self.assertEqual(total_entries, tile_total)



    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(
            testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/kimbo/PycharmProjects/selenium/Demo/reports'))
        # unittest.main(verbosity=2)
