import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


URL = "https://tinder.com/"

load_dotenv(dotenv_path=".env")
username=os.getenv("mail")
password = os.getenv("password")

def driver_initialization (url : str):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    inner_driver = webdriver.Chrome(options=chrome_options)
    inner_driver.get(url)
    return inner_driver

driver = driver_initialization(URL)


sleep(3)
login = driver.find_element(By.LINK_TEXT, "Log in")

login.click()

sleep(3)

accept_buttons = driver.find_elements(By.CSS_SELECTOR, value="div div div div div button")

accept_buttons[8].click()

facebook_button = driver.find_element(By.XPATH, value='//*[@id="q18919352"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
facebook_button.click()


base_window = driver.window_handles[0]

fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

sleep(2)



fb_cookies = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div')
fb_cookies.click()

fb_login = driver.find_element(By.ID, value="email")
fb_pass = driver.find_element(By.ID, value="pass")
login_button = driver.find_element(By.NAME, value="login")

fb_login.send_keys(username)
fb_pass.send_keys(password)
login_button.click()
sleep(8)

classes_string = "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft".split()

next_buttons = driver.find_elements(By.XPATH, value="//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft']")


next_buttons[0].click()

sleep(7)

driver.switch_to.window(base_window)

# first pop up window
buttons =driver.find_elements(By.XPATH, value= "//button[@class='c1p6lbu0 W(100%)']")
sleep(4)
buttons[0].click()

sleep(5)

buttons_miss_out =driver.find_elements(By.XPATH, value= "//div[@class='lxn9zzn']")

buttons_miss_out[1].click()

# we are in

sleep(2)

down_buttons = driver.find_elements(By.XPATH, value="//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style gamepad-button Bxsh($bxsh-btn) Expand Ov(h) Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-nope):a']")

for i in range(10):
    # driver.find_element(By.XPATH, value="//div[@class='lxn9zzn'").click()
    #     not_intersted.click()
    try:
        sleep(1)
        not_intersted = driver.find_element(By.XPATH, value="//div[@class='lxn9zzn']")
        not_intersted.click()
    except:
        down_buttons[0].click()
        sleep(2)
