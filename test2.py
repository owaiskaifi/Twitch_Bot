from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
 


username = ""
password = ""
email = ""
lower_upper_alphabet = string.ascii_letters
for i in range(10):
    username =  username + random.choice(lower_upper_alphabet)
print(username)
chrome = webdriver.Firefox( )

chrome.get("https://10minemail.com/en/")

getemail = chrome.find_element_by_xpath("//input[@id='mail']")
email = getemail.get_attribute("value")
time.sleep(2)
print(email)

chrome.get("https://twitch.tv")

signup = chrome.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button/div/div")
signup.click()
time.sleep(3)

uname = chrome.find_element_by_xpath("//input[@id='signup-username']")
uname.send_keys(username + "urmomgay")
password = username + "utizver"

pass1 = chrome.find_element_by_xpath("//input[@id='password-input']")
pass1.send_keys(password)

pass2 = chrome.find_element_by_xpath("//input[@id='password-input-confirmation']")
pass2.send_keys(password)

month = Select(chrome.find_element_by_xpath("//select[@data-a-target='birthday-month-select']"))
month.select_by_visible_text("January");  

day = chrome.find_element_by_xpath("//input[@aria-label='Enter the day of your birth']")
day.send_keys("11")

year = chrome.find_element_by_xpath("//input[@placeholder='Year']")
year.send_keys("1985")

emailinput = chrome.find_element_by_xpath("//input[@type='email']")
emailinput.send_keys(email)

time.sleep(2)

sub = chrome.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button")
sub.click()

time.sleep(8)
