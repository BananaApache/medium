

"""FILE TEST"""
# from bs4 import BeautifulSoup as bs

# with open('index.html', 'r') as f:
#     soup = bs(f, 'html.parser')

# for name in soup.find_all("img"):
#     print(name)

# f = open("follow_count.txt", 'w')
# f.write('64')


"""FOLLOWER TEST"""
# follower_count = "11.2K Followers"
# follower_count = str(follower_count).split()[0]
# if follower_count.endswith("K"):
#     follower_count = int(float(follower_count[:follower_count.find("K")]) * 1000)


"""SCROLLING TEST"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from time import sleep as s
# import pyautogui as pg
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# driver = webdriver.Chrome(service=Service(
#     "chromedriver"), options=chrome_options)


# def scroll(pause_time):

#     # Get scroll height
#     last_height = driver.execute_script("return document.body.scrollHeight")

#     for _ in range(3):
#         # Scroll down to bottom
#         driver.execute_script(
#             "window.scrollTo(0, document.body.scrollHeight);")

#         # Wait to load page
#         s(pause_time)

#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height


# driver.get("https://medium.com/@avikotzer/followers")

# s(2)

# followed = 0
# loop = 0

# while True:

#     print(f"follower in range({10 * loop + 1, 10 * loop + 11})")

#     for follower in range(10 * loop + 1, 10 * loop + 11):
#         follow_button = driver.find_element(by=By.XPATH, value=f'//*[@id="root"]/div/div[3]/div[2]/div/main/div/div/div/div[3]/ul/div[{follower}]/div/div/button')
        
#         if follow_button.text == "Follow":
#             follow_button.click()
#             s(0.6)

#         followed += 1
#         print(follower)

#     pg.scroll(-22)

#     loop += 1


"""FILE TEST"""

def open_file():
    # Opens count file
    f = open('follow_count.txt', 'r')
    count = int(f.read())
    print(count)

    # Writes new count to file
    count += 1
    f = open('follow_count.txt', 'w')
    f.write(str(count))
    f.close()

    inp = input("Increase count? ")
    if inp == "y":
        open_file()


open_file()
