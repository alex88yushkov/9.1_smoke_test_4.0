from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By # Alexander Yushkov -- 05/22/21
from selenium.webdriver.support.ui import WebDriverWait # Alexander Yushkov -- 05/22/21
from selenium.webdriver.support import expected_conditions as EC # Alexander Yushkov -- 05/22/21
from selenium.webdriver.support.select import Select # Alexander Yushkov -- 05/22/21

from BrainBucket.webelements.browser import Browser # Alexander Yushkov -- 05/23/21
from BrainBucket.webelements.UIElement import UIElement as Element # Alexander Yushkov -- 05/23/21
import time

browser = Browser("https://techskillacademy.net/brainbucket/index.php?route=account/login") # Alexander Yushkov -- 05/23/21
driver = browser.get_driver() # Alexander Yushkov -- 05/23/21
wait = browser.get_wd_wait() # Alexander Yushkov -- 05/23/21

driver.maximize_window()

# LOGIN PAGE
Element(browser, By.XPATH, "//img[@title='Brainbucket']") # Alexander Yushkov -- 05/23/21

# Alexander Yushkov -- 05/09/21
# password_field = driver.find_element_by_id("input-password")
Element(browser, By.ID, "input-password").enter_text("123qwe123qweasdzc") # Alexander Yushkov -- 05/23/21


# Alexander Yushkov -- 05/09/21
# login_btn = driver.find_element_by_xpath("//input[@value='Login']")
Element(browser, By.XPATH, "//input[@value='Login']").click() # Alexander Yushkov -- 05/23/21

time.sleep(1)

# Alexander Yushkov -- 05/09/21
Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]").click() # Alexander Yushkov -- 05/23/21

# Register Account PAGE

wait.until(EC.title_is("Register Account")) # Alexander Yushkov -- 05/22/21

# Alexander Yushkov -- 05/09/21
fields = [("2", "firstname", "Alexander"), ("3", "lastname", "Yushkov"),
          ("4", "email", "test@test.com"), ("5", "telephone", "123-123-1231")]
# Alexander Yushkov -- 05/09/21
for field in fields:
    some_field = Element(browser, By.XPATH, "//fieldset/div[%s]" % field[0]) # Alexander Yushkov -- 05/23/21
    field_input = Element(browser, By.ID, 'input-%s' % field[1]) # Alexander Yushkov -- 05/23/21
    field_class = some_field.get_attribute("class") # Alexander Yushkov -- 05/23/21
    assert "required" in field_class

    field_input.enter_text("%s" % field[2])

fax_field = Element(browser, By.XPATH, "//fieldset/div[6]") # Alexander Yushkov -- 05/23/21
fax_input = Element(browser, By.ID, 'input-fax') # Alexander Yushkov -- 05/23/21
fax_field_class = fax_field.get_attribute("class") # Alexander Yushkov -- 05/23/21
assert "required" not in fax_field_class

fax_input.enter_text("321-543-9877") # Alexander Yushkov -- 05/23/21

################### Exercise #1
# Alexander Yushkov -- 05/22/21:
state_dropdown = driver.find_element_by_id("input-zone")
state_dropdown_select = Select(state_dropdown)
state_dropdown_select.select_by_value("3635") # Illinois

policy_box = driver.find_element_by_xpath("//input[@name='agree' and @value='1']")
if not policy_box.is_selected():
    policy_box.click()

subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
if not subscribe_btn.is_selected():
    subscribe_btn.click()
################### /Exercise #1
time.sleep(1)
################### Exercise #2:
# Alexander Yushkov -- 05/22/21
Element(browser, By.XPATH, "//a[@title='My Account']").click() # Alexander Yushkov -- 05/23/21

Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']").wait_until_visible() # Alexander Yushkov -- 05/23/21

Element(browser, By.XPATH, "//a[contains(text(),'Register')]").click() # Alexander Yushkov -- 05/23/21

reg_page_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/h1"))) # Alexander Yushkov -- 05/23/21
assert reg_page_header.text == "Register Account"

Element(browser, By.XPATH, "//a[@title='My Account']").click() # Alexander Yushkov -- 05/23/21
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']"))) # Alexander Yushkov -- 05/23/21

Element(browser, By.XPATH, "//a[contains(text(),'Login')]").click() # Alexander Yushkov -- 05/23/21

wait.until(EC.title_is("Account Login")) # Alexander Yushkov -- 05/23/21
################### /Exercise #2

time.sleep(1)
driver.close()