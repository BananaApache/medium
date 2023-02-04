
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

# driver.get('https://medium.com/m/signin')
# s(2)

# Checks if already signed in
# if driver.current_url != "https://medium.com/":
#     signin_with_google = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div/div[2]/a")
#     signin_with_google.click()

#     pg.write("Jack.jiaen.he@gmail.com")
#     next = driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button')
#     next.click()
#     s(1)

#     pg.write("{Rhona@0123}{Jack@0603}")
#     next = driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button')
#     next.click()
#     s(5)

def get_followers():

    driver.get('https://medium.com/@jack.he/followers')

    s(2)

    loop = 0

    while True:
        for i in range(10 * loop + 1, 10 * loop + 11):
            name = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{i}]/div/a/div/div[1]/h2/span').text
            f = open('jacks_followers.txt', 'a')
            f.write(name + "\n")
            print(name, "added!")
            f.close()
            s(0.1)

        pg.scroll(-150)
        s(1)
        pg.scroll(-150)
        s(1)
        pg.scroll(-150)
        loop += 1


def unfollow_people():
    driver.get('https://medium.com/@jack.he')
    s(2)

    see_all = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[5]/p/button')
    see_all.click()

    loop = 0

    while True:
        for i in range(5 * loop + 1, 5 * loop + 6):
            if i == 1:
                continue

            print(i)

            name = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div/div[1]/div/div[{i}]/div/div[1]/div[2]/a/div/h2').text
            if name not in open('jacks_followers.txt', 'r').read():
                print(name, "unfollowed")
                unfollow = driver.find_element(by=By.XPATH, value=f'/html/body/div[2]/div/div[1]/div/div[{i}]/div/div[2]/button')
                driver.execute_script("arguments[0].click();", unfollow)

        try:
            show_more = driver.find_element(By.CLASS_NAME, 'bc.b.bd.y.bh.ub.ln.rl.ur.dr.us.am.un.uo.up.dd.bj.mx')
            driver.execute_script("arguments[0].click();", show_more)
            s(2)
        except:
            pass

        loop += 1


unfollow_people()
