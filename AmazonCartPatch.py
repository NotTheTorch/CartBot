from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

global browser 
browser= webdriver.Chrome()
browser.get("https://www.google.com") 
wait = WebDriverWait(browser,45)
search = browser.find_element(By.NAME,"q") 
search.send_keys("Amazon")
search.send_keys(Keys.RETURN) 
wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"amazon.in"))).click()
search = wait.until(EC.presence_of_element_located((By.ID,"twotabsearchtextbox"))) 
search.send_keys("PS5") 
search.send_keys(Keys.RETURN)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Sony PS5 PlayStation Console"))).click()
new_tab= browser.window_handles[-1]
browser.switch_to.window(new_tab)
try:
    add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    add_to_cart_button.click()
except Exception as e:
    print("Error:", e)

print("Time Taken:",time.time())

time.sleep(2)
browser.quit()