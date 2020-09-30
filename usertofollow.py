from time import sleep
from selenium import webdriver

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

username_input.send_keys("ENTER YOUR USERNAME HERE  ")
password_input.send_keys("ENTER YOUR PASSWORD HERE")

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

# search your niche
search_input = browser.find_element_by_xpath(
    '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
search_input.send_keys("ufkappadelta") #PLEASE ENTER THE ACCOUNT YOU WANT TO STEAL FOLLOWERS FROM 
sleep(2)

click_florida = browser.find_element_by_xpath(
    '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span')
click_florida.click()
sleep(3)

# gotofollowers
the_followers = browser.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
the_followers.click()
sleep(2)


# find all li elements in list
fBody = browser.find_element_by_xpath("//div[@class='isgrP']")
scroll = 0
while scroll < 300:  #AMOUNT OF PEOPLE 
    browser.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    sleep(3)
    scroll += 1

fList = browser.find_elements_by_xpath("//div[@class='isgrP']//li")
print("fList len is {}".format(len(fList)))

print("Scroll down ended brotha")




scrollUp = 0
while scrollUp < 300:  #AMOUNT OF POEPLE
    browser.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;', fBody)
    sleep(3)
    scrollUp += 1

fListSecond = browser.find_elements_by_xpath("//div[@class='isgrP']//li")
nameList = browser.find_elements_by_tag_name('a')
print("fList len is {}".format(len(fListSecond)))

print("Scroll Up ended brotha")

#THIS WILL PRINT ALL THE POEPLE FOLLOWING THE NICHE SELECTED
names = [name.text for name in nameList if name.text != '']
print(names)

#COPY ALL THE USERNAMES ON PROMT AND PASTED IN ARRAY 



