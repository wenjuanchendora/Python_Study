"""
cnodejs 发帖操作
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://118.31.19.120:3000/signin")

driver.find_element_by_id("name").send_keys("username")
driver.find_element_by_id("pass").send_keys("password")

driver.find_element_by_class_name("span-primary").click()

driver.find_element_by_id("create_topic_btn").click()

driver.find_element_by_id("tab-value").click()

driver.find_element_by_css_selector("#tab-value > option:nth-child(3)").click()

driver.find_element_by_id("title").send_keys("12345")

# 写入文本内容

# drvier.find_element_by_css_selector("#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll").send_keys("abcde")
contentInput = driver.find_element_by_css_selector("#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll")
ActionChains(driver).move_to_element(contentInput).click().perform()
contentArea = driver.find_element_by_css_selector("#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre")
ActionChains(driver).move_to_element(contentArea).send_keys("abcde").perform()

# driver.find_element_by_class_name("span-primary submit_btn").click()