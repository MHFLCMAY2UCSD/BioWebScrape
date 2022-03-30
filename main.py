import time
import random
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    PATH = '/Users/theaccount/opt/anaconda3/envs/WebScraping/chromedriver'
    driver = webdriver.Chrome(PATH)

    driver.get("https://lrccd.instructure.com/courses/125588/quizzes")

    time.sleep(6)

    # Login Process
    username = driver.find_element_by_id("username")
    username.send_keys("w1777471")

    time.sleep(random.randint(3, 8))

    password = driver.find_element_by_id("password")
    password.send_keys("California95682")

    time.sleep(random.randint(2, 5))

    login_in = driver.find_element_by_name("_eventId_proceed")
    login_in.click()

    time.sleep(4)

    # Go time
    head = "Week "
    body = " Quiz"
    amount = 14
    for i in range(amount + 1):
        if i > 1:
            insert = head + str(i) + body
            quiz = driver.find_element_by_link_text(insert)
            quiz.click()

            result = requests.get(driver.current_url)

            soup = bs4.BeautifulSoup(result.text, "lxml")



        else:
            print("Wuba-luba dub-dub")

    time.sleep(2)

    driver.quit()


main()

