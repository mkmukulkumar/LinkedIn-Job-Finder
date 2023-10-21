import time
from credentials import secrets
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def open_site(driver):
    print("site open")
    driver.get('https://www.linkedin.com') 

def maximize(driver):
    print("maximizing the window")
    driver.maximize_window()

def login(driver,username,password):
    time.sleep(6)         
    element=driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input")                               
    element.send_keys(username)
    element=driver.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)
    time.sleep(6)
    cookies=driver.get_cookies()
    pickle.dump(cookies, open("cookies.pkl", "wb"))



if __name__=="__main__":
    webdriverpath="D:\Software\chromedriver.exe"
    driver = webdriver.Chrome()
    open_site(driver)
    maximize(driver)
    username=secrets.get('username')
    password=secrets.get("password")
    login(driver,username,password)
    while(1):
        pass
