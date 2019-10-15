class Users:


    def __init__(self, driver):
        self.driver = driver
        self.page_display_options_xpath =".//*[normalize-space(text()) and normalize-space(.)='Jul 10th 2018, 02:07:52 AM'])[1]/following::div[5]"
        self.header_1 = "(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::span[1]"
        self.header_2 = "(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::span[2]"
        self.header_3 = "(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::span[3]"
        self.header_4 = "(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::span[4]"

    def get_row_count(self):
        list_items = self.driver.find_elements_by_class_name("MuiTableRow-hover")
        items_count = len(list_items)
        return items_count

    def get_header(self, header_number):
        self.driver.get('https://sb-qawebtest.azurewebsites.net/users')
        text_found = self.driver.find_element_by_xpath(header_number).text
        return text_found

