class HomePage():

    def __init__(self, driver):

        self.driver = driver

        self.home_button_xpath = "//*[@id='root']/div/div[1]/header/div/h6[1]/a"
        self.computers_button_xpath = "//*[@id='root']/div/div[1]/header/div/h6[2]/a"
        self.users_button_xpath = "//*[@id='root']/div/div[1]/header/div/p/a"

    def go_to_page(self, xpath):
        self.driver.get('https://sb-qawebtest.azurewebsites.net/')
        self.driver.find_element_by_xpath(xpath).click()

