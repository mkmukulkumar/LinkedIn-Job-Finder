import time
from credentials import secrets
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def scrollbottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
    time.sleep(5)

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
    print("cookies saved")

def logincookies(driver):
    time.sleep(6)         
    cookies=pickle.load(open("cookies.pkl","rb"))
    for cookie in cookies:
        cookie['domain']=".linkedin.com"
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)   
    print("Cookies loaded")
    time.sleep(8)
    driver.get("https://www.linkedin.com/in/mkmukulkumar/details/interests/")        

def getcompanies(driver):
    time.sleep(5)
    i=1
    last=0
    companylist=[]
    while(1):
        try:
            element=driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[1]/ul/li["+str(i)+"]/div/div/div[2]/div[1]/a/div/div/div/div/span[1]")
            company=element.text
            element=driver.find_element(By.XPATH,"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[1]/ul/li["+str(i)+"]/div/div/div[2]/div[1]/a")
            companyurl=element.get_attribute("href")
            companylist.append([company,companyurl])
            i=i+1
            print(i)

        except Exception as e:
            curr=driver.execute_script("return document.body.scrollHeight;")
            if(last!=curr):
                last=curr
                scrollbottom(driver)
            else:
                break       
    return companylist

def getjobs(driver,companylist):
        j=0
        print("getjob")
        for name,url in companylist:
            recomjobs=[]
            recentjobs=[]
            try:
                driver.get(url+"/jobs/")
                time.sleep(3)
                driver.execute_script("window.scrollTo(0, 720);")
            except Exception as e:
                continue    
            i=1
            while(i<=3):
                try:
                    recomjob=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/section[2]/div/section[1]/div[2]/ul/li["+str(i)+"]/div/div/div/section/div/a/div[1]/div[2]/div[1]/div/span")
                    recomjobs.append(recomjob.text)
                except Exception as e:
                    print(e)
                    break
                i=i+1
            i=1
            while(i<=3):    
                try:
                    recentjob=driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[2]/section/div[2]/ul/li["+str(i)+"]/div/div/div/section/div/a/div[1]/div[2]/div[1]/div/span")
                    recentjobs.append(recentjob.text)
                except Exception as e:
                    
                    print(e)
                    break
                i=i+1
            companylist[j].append(recomjobs)
            companylist[j].append(recentjobs)
            j=j+1
            print(companylist)
        return companylist    

if __name__=="__main__":
    webdriverpath="D:\Software\chromedriver.exe"
    driver = webdriver.Chrome()
    open_site(driver)
    maximize(driver)
    username=secrets.get('username')
    password=secrets.get("password")
    # login(driver,username,password)
    logincookies(driver)
    companylist=getcompanies(driver)
    companylist=getjobs(driver,companylist)
    print(companylist)
    while(1):
        pass
