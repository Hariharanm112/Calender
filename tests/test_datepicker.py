import time

import pytest
from selenium.webdriver.common.by import By
from project.page.datepicker_page import DatePickerpage

@pytest.mark.parametrize("monthy_click,day",[
    (0,"1"),
    (2,"15"),
    (1,"30")
])

def test_selectdate(browser,monthy_click,day):
    browser.get("https://jqueryui.com/datepicker/")
    iframe=browser.find_element(By.CLASS_NAME,"demo-frame")
    browser.switch_to.frame(iframe)
    page=DatePickerpage(browser)
    page.open_datepicker()
    page.click_next(time=monthy_click)
    page.select_date(day)
    selected=page.get_selected_date()
    print(selected)
    time.sleep(10)
    assert selected != "","no date was selected"

