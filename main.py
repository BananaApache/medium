
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

driver = webdriver.Chrome(executable_path="chromedriver", options=chrome_options)

driver.get('https://medium.com/m/signin')
print("\nNavigating to https://medium.com/")
s(2)

# Checks if already signed in
if driver.current_url != "https://medium.com/":
    print("Signing in...")
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

print("Sign in complete")

print("Switching to Chrome Tab...")

pg.keyDown("alt")
pg.press("tab")
pg.keyUp("alt")

FOLLOW_COUNT = 0

def open_profile():
    global FOLLOW_COUNT
    if FOLLOW_COUNT > 125:
        pg.keyDown("alt")
        pg.press("tab")
        pg.keyUp("alt")
        print("\nFollowed the Maximum of 125 people\n")
        exit()
    
    # Opens count file
    f = open('follow_count.txt', 'r')
    count = int(f.read())

    # Opens profile
    print("\nGetting next follower...\n")
    driver.get("https://medium.com/@jack.he/followers")

    try:
        follower = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{count}]/div/a')
        name = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{count}]/div/a/div/div[1]/h2/span').text
        print(f"FOUND FOLLOWER: {name}\n")
        driver.execute_script("arguments[0].click();", follower)
        s(1)

    except:
        s(1)
        for i in range(int(count / 3)):
            driver.execute_script("window.scrollTo(0, 6000)")
            s(1)

        s(2)
        follower = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{count}]/div/a')
        name = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{count}]/div/a/div/div[1]/h2/span').text
        print(f"FOUND FOLLOWER: {name}\n")
        driver.execute_script("arguments[0].click();", follower)

    try:
        s(1)
        follower_page = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/span/a')
        follower_page.click()
        s(1)
    except:
        s(3)
        follower_page = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/span/a')
        follower_page.click()
        s(2)

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
        print(f"{name} has a bunch of followers")
        print(f"Starting to loop...\n")
        # Starts looping here
        loop = 0
        
        while True:
            for follower in range(10 * loop + 1, 10 * loop + 11):
                try:
                    follow_button = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{follower}]/div/div/button')
                    follow_name = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{follower}]/div/a/div/div[1]/h2/span').text
                    
                    if follow_button.text == "Follow":
                        # follow_button.click()
                        driver.execute_script("arguments[0].click();", follow_button)
                        print(f"!!! FOLLOWED {follow_name} !!!")
                        FOLLOW_COUNT += 1
                
                        s(0.3)
                    else:
                        print(f"--- {follow_name} already follows you ---")
                except:
                    open_profile()

            pg.scroll(-22)

            loop += 1


    else:
        print("\nToo little followers, moving to next person...\n")
        open_profile()
        

try:
    open_profile()
except Exception as e:
    pg.keyDown("alt")
    pg.press("tab")
    pg.keyUp("alt")

    print(e)
    print("\n\nSomething bad happened\n")
    print("Screenshot error and send to me so i can fix\n")

