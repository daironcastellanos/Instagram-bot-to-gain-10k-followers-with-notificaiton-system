from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import cycle


browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')


sing_up = browser.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span')
sing_up.click()
sleep(2)

# goto log in window
log_in = browser.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[2]/p/a')
log_in.click()
sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("ENTER YOUR USERNAME HERE ")
password_input.send_keys("ENTER YOUR PASSWORD HERE ")

login_button = browser.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]')
login_button.click()

sleep(2)

# NOTNOWBUTTON
not_now = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div/div/div/button')
not_now.click()
sleep(2)

# notifications
notifications_off = browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]')
notifications_off.click()
sleep(2)

# PASTE THE PEOPLE YOU WANT TO FOLLOW IN HERE
names = ['CRISTIANO RONALDO','LEONEL_MESSI']


i = 0
amount = 0


while amount < 180:  # AMOUNT OF PEOPLE TO FOLLOW EVERY DAY
    print(names[i])
    search_input = browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search_input.send_keys(names[i])
    enter_account = browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div')
    enter_account.click()
    # sleep(3)
    # search_input.send_keys(u'\ue007')
    # sleep(3)
    # search_input.send_keys(u'\ue007')
    sleep(3)
    follow_this = browser.find_element_by_xpath(
        "//*[text()='Follow']")
    follow_this.click()
    # sleep(3)
    # browser.execute_script("window.history.go(-1)")
    sleep(5)  # HOW LONG INSTAGRAM WAITS TO FOLLOW ANOTHER POPLE
    i += 1
    amount += 1
    print("You followed: " + str(amount) + " so far")

browser.get('https://www.opentextingonline.com/')
# NOTIFICATION SYSTEM
# open mail
sleep(3)
phone_input = browser.find_element_by_xpath(
    '/html/body/div[1]/main/section/div[2]/div[1]/form/div[1]/div[1]/div[1]/input')
data_input = browser.find_element_by_xpath(
    '/html/body/div[1]/main/section/div[2]/div[1]/form/div[5]/div[1]/textarea')

phone_input.send_keys("PUT YOUR PHONE NUMBER HERE ")
data_input.send_keys("iNsTaBoT Action Completed: " + str(amount) + " Followed")
sleep(5)
click_send = browser.find_element_by_xpath(
    '/html/body/div[1]/main/section/div[2]/div[1]/form/div[6]/div[1]/button')
click_send.click()
sleep(1)
click_send.click()
sleep(3)
ok_button = browser.find_element_by_xpath(
    '/html/body/div[1]/main/section/div[8]/div/div/div[3]/div/button')
ok_button.click()
sleep(1)
ok_button.click()
sleep(5)
