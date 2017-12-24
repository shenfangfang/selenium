from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")

# 打印当前页面title
title = driver.title
print("准备登陆，当前页面title是：%s" %title)

#登录 方法依次是跳转某个iframe；退出到父iframe；跳出所有iframe，退出到主页面
# driver.switch_to.frame(reference)
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()

time.sleep(1)
driver.switch_to.frame('login_frame')
driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("********")#这里写上QQ号码
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys("********") #这里写上密码
driver.find_element_by_id("login_button").click()
driver.switch_to.default_content()

# 打印当前页面URL
now_url = driver.current_url
print("登陆成功，当前页面的url是：%s" %now_url)

# 发送邮件
time.sleep(1)
driver.find_element_by_id("composebtn").click()
driver.switch_to.frame("mainFrame")
time.sleep(1)
driver.find_element_by_id("toAreaCtrl").find_element_by_class_name("js_input").send_keys("******@aliyun.com")#输入接收邮箱
driver.find_element_by_id("subject").clear()
driver.find_element_by_id("subject").send_keys("邮件标题，这是一份测试邮件")
driver.switch_to.frame(driver.find_element_by_class_name("qmEditorIfrmEditArea"))
driver.find_element_by_tag_name('body').send_keys("邮件正文")
#退回父iframe：mainFrame
driver.switch_to.parent_frame()
time.sleep(1)
driver.find_element_by_link_text(u"发送").click()
print("发送成功")
#退出iframe
driver.switch_to.default_content()
time.sleep(1)
driver.find_element_by_link_text(u"退出").click()
print("退出url")
driver.quit()