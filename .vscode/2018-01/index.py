import random
from selenium import webdriver

# 设置浏览器
# for mac user
# drvier = webdriver.Chrome(executable_path="./chromedriver")
# for winwow users
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("https://www.baidu.com/")

# 找打搜索框元素
baiduserach =  browser.find_element_by_id("kw")
# list = ['a','b','c','d']
# random.shuffle(list)
# 输入文字
baiduserach.send_keys("hello world")