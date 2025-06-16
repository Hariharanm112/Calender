
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DatePickerpage:
    def __init__(self,driver):
        self.driver=driver
        self.datepicker_input=(By.ID,"datepicker")
        self.next_button=(By.XPATH,"//a[@title='Next']")




    def open_datepicker(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,"datepicker"))).click()

    def click_next(self,time=2):
        for i in range(time):
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Next']"))).click()

    def select_date(self,day):
        xpath=f"//a[text()='{day}']"
        self.driver.find_element(By.XPATH,xpath).click()

    def get_selected_date(self):
        return self.driver.find_element(*self.datepicker_input).get_attribute("value")