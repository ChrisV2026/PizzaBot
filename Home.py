from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("chromedriver.exe")

driver.get('https://www.dominos.ca/pages/order/#!/locations/search/?type=Delivery')

City_form= driver.find_element_by_id("City")

Atype_select = Select(driver.find_element_by_id("Address_Type_Select"))

Atype_select.select_by_index(0) 

Continue_for_Delivery = driver.find_element_by_class_name("btn--search-location")

City_form.send_keys("Mississauga")

Continue_for_Delivery.click()