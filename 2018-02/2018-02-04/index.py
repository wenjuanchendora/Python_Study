from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver =  webdriver.Chrome()

driver.get("https://account.aliyun.com/register/register.htm")

# switch to iframe

driver.switch_to_frame('alibaba-register-box')

# find element

dragdiv = driver.find_element_by_id("nc_1_n1z")

# create  action--- drag_and_drop_by_offset

ActionChains(driver).drag_and_drop_by_offset(dragdiv,400,400).perform()

