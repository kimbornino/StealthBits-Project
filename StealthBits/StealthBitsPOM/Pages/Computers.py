class Computers():

    def __init__(self, driver):
        self.driver = driver
        self.page_display_options_xpath =".//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::div[5]"
        self.header_1 = "//*[@id='root']/div/div[2]/div[1]/table/thead/tr/th[1]/span"
        self.header_2 = "//*[@id='root']/div/div[2]/div[1]/table/thead/tr/th[2]/span"
        self.header_3 = "//*[@id='root']/div/div[2]/div[1]/table/thead/tr/th[3]/span"
        self.header_4 = "//*[@id='root']/div/div[2]/div[1]/table/thead/tr/th[4]/span"
        self.header_5 = "//*[@id='root']/div/div[2]/div[1]/table/thead/tr/th[5]/span"
    def get_row_count(self):
        list_items = self.driver.find_elements_by_class_name("MuiTableRow-hover")
        items_count = len(list_items)
        return items_count

    def get_header(self, header_number):
        self.driver.get('https://sb-qawebtest.azurewebsites.net/computers')
        text_found = self.driver.find_element_by_xpath(header_number).text
        return text_found