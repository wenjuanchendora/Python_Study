# code v0.0.1

"""Test_Case_01: 检查必填项全为空的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在注册界面不做任何输入，直接点击 “提交” 按钮
Expected_Result:
系统提示：信息不完整。
"""


"""Test_Case_02: 检查必填项 “用户名” 不符合要求的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在 “用户名” 文本框中输入 “123”
4. 在 “密码” 文本框中输入 “password”
5. 在 “确认密码” 文本框中输入 “password”
6. 在 “电子邮箱” 文本框中输入 “123456789@qq.com”
7. 点击 “提交” 按钮
Expected_Result:
系统提示：用户名至少需要5个字符。
"""


"""Test_Case_03: 检查必填项全符合要求的情况
Steps:
1. 打开浏览器，输入论坛网址，点击回车键
2. 点击首页中的 “注册” 按钮
3. 在 “用户名” 文本框中输入 “username”
4. 在 “密码” 文本框中输入 “password”
5. 在 “确认密码” 文本框中输入 “password”
6. 在 “电子邮箱” 文本框中输入 “123456789@qq.com”
7. 点击 “提交” 按钮
Expected_Result:
系统提示：欢迎加入 Nodeclub！我们已给您的注册邮箱发送了一封邮件，请点击里面的链接来激活您的帐号。
"""

from selenium import webdriver
import time

# username=['','123','username']
# password=['','12345','password']
# repasswd=['','12345','password']
# email=['','12345@qq.com','123456789@qq.com']
# driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# def register(username,password,repasswd,email):
#     # 打开 Cnode 论坛网址
#     driver.get("http://118.31.19.120:3000/")

#     # 点击注册
#     regis = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul/li[5]/a')
#     regis.click()
#     # 输入用户名
#     usernameInput = driver.find_element_by_id("loginname")
#     usernameInput.send_keys(username)
#     # 输入密码
#     passwordInput = driver.find_element_by_id("pass")
#     passwordInput.send_keys(password)
#     # 确认密码
#     confirmpass = driver.find_element_by_id("re_pass")
#     confirmpass.send_keys(repasswd)
#     # 输入电子邮箱
#     emailInput = driver.find_element_by_id("email")
#     emailInput.send_keys(email)
#     # 点击注册
#     cnoderegis = driver.find_element_by_class_name("span-primary")
#     cnoderegis.click()

    # time.sleep(3)

    # tipmsg = driver.find_element_by_class_name("alert alert-error").text()
    # print(tipmsg)

# for i in range(3):
#     register(username[i],password[i],repasswd[i],email[i])
# driver.quit()


test_data=[
    ['xiaoming','123456','123456','xm@1234.com'],
    ['','123456','123456','xm@1234.com'],
    ['xiaoming','','123456','xm@1234.com'],
    ['xiaoming','123456','','xm@1234.com']
]

drvier = webdriver.Chrome()

def regitser(username,passwd,repasswd,email):

    # 打开Node注册页面
    drvier.get("http://118.31.19.120:3000/")
    # 注册 register
    registerXpath = "/html/body/div[1]/div/div/ul/li[5]/a"
    registerLink = drvier.find_element_by_xpath(registerXpath)
    registerLink.click()

    # 输入用户名
    usermaneinput = "loginname"
    username_input_area = drvier.find_element_by_id(usermaneinput)
    username_input_area.send_keys(username)

    # 输入密码
    pwdinput = "pass"
    pwd = drvier.find_element_by_id(pwdinput)
    pwd.send_keys(passwd)

    # 输入确认密码
    repwdinput = "re_pass"
    repwd = drvier.find_element_by_id(repwdinput)
    repwd.send_keys(repasswd)

    # 输入邮箱地址
    emailinput = "email"
    email_area = drvier.find_element_by_id(emailinput)
    email_area.send_keys(email)

    # 点击注册按钮
    registerBot = "span-primary"
    rigerterbtn = drvier.find_element_by_class_name("span-primary")
    rigerterbtn.click()

    filename = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    drvier.save_screenshot(filename + '.png')

    # time.sleep(6)

    # tipmsg = drvier.find_element_by_class_name('alert alert-error').text()

    # print(tipmsg)


for x in range(len(test_data)):
    regitser(test_data[x][0],test_data[x][1],test_data[x][2],test_data[x][3])


drvier.quit()



# for i in range(len(test_data)):
#     # for j in range(len(test_data[i])):
#         # print(i,':',j,'-->',test_data[i][j])
#     register(test_data[i][0],test_data[i][1],test_data[i][2],test_data[i][3])
