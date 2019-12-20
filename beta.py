from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

##for mac need ./ and no exe for chromedriver
driver = webdriver.Chrome("./chromedriver")
#driver.get('https://www.dominos.ca/pages/order/#!/locations/search/?type=Delivery')
driver.get('https://www.dominos.ca')



#element = driver.find_element_by_xpath("//*[@id="homeWrapper"]/main/section[1]/div/div[2]/a[1]").click()
driver.find_element_by_class_name("btn smart-order__cta").click()

City_form = driver.find_element_by_id("City")



Atype_select = Select(driver.find_element_by_id("Address_Type_Select"))
Atype_select.select_by_index(0)

Street = driver.find_element_by_id("Street")

Continue_for_Delivery = driver.find_element_by_class_name("btn--search-location")

City_form.send_keys("Mississauga")

Continue_for_Delivery.click()
