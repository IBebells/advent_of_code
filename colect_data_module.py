# Libarys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def sing_in_github (driver: webdriver):
    # Credentials
    email = 'xxxxxxxx@xxxxx.com'
    password = 'XXXX'
    
    # Acess autentication website
    driver.get('https://adventofcode.com/auth/github')

    # Insert e-mail
    driver.find_element(By.XPATH, '//*[@id="login_field"]').\
        send_keys(email)

    # Insert password
    driver.find_element(By.XPATH, '//*[@id="password"]').\
        send_keys(password)

    # Click in Sing in button
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[13]').\
        click()


def colet_puzzle_input(driver: webdriver, url: str) -> str:

    time.sleep(5)

    # Acess data website
    driver.switch_to.new_window('tab')

    driver.get(url)

    puzzle_input = driver.find_element(By.XPATH, '/html/body').text

    driver.quit()

    return puzzle_input

