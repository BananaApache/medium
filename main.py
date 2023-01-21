
#~ WITH SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep as s
import pyautogui as pg
from bs4 import BeautifulSoup as bs

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(service=Service("chromedriver"), options=chrome_options)

driver.get('https://medium.com/m/signin')
s(2)

# Checks if already signed in
if driver.current_url != "https://medium.com/":
    signin_with_google = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/div[2]/a")
    signin_with_google.click()

    pg.write("Jack.jiaen.he@gmail.com")
    next = driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button')
    next.click()
    s(1)

    pg.write("{Rhona@0123}{Jack@0603}")
    next = driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button')
    next.click()
    s(5)


def open_profile():
    # Opens count file
    f = open('follow_count.txt', 'r')
    count = int(f.read())

    # Opens profile
    driver.get("https://medium.com/@jack.he/followers")

    follower = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{count}]/div/a')
    follower.click()
    s(1)

    follower_page = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/span/a')
    follower_page.click()
    s(1)

    # Gets follower info
    follower_name = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/a/h2/span').text
    follower_count = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/span').text
    follower_count = str(follower_count).split()[0]
    
    # Writes new count to file
    count += 1
    f = open('follow_count.txt', 'w')
    f.write(str(count))
    f.close()

    # Checks how many followers
    if follower_count.endswith("K"):
        # Starts looping here
        followed = 0
        loop = 0
        
        while True:
            if followed > 125:
                print("\nFollowed 125 people\n")
                exit()

            for follower in range(10 * loop + 1, 10 * loop + 11):
                try:
                    follow_button = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{follower}]/div/div/button')
                    follow_name = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{follower}]/div/a/div/div[1]/h2/span').text
                    
                    if follow_button.text == "Follow":
                        # follow_button.click()
                        driver.execute_script("arguments[0].click();", follow_button)
                        print(f"!!! FOLLOWED {follow_name} !!!")
                        followed += 1
                
                        s(0.3)
                    else:
                        print(f"--- {follow_name} already follows you ---")
                except:
                    open_profile()

            pg.scroll(-22)

            loop += 1


    else:
        open_profile()
        

open_profile()
