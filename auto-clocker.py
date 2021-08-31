from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get('https://omnibpm.com/login/')

account_xpath = '//*[@id="app"]/div/div[1]/div/div[2]/form/div[1]/input'
password_xpath = '//*[@id="app"]/div/div[1]/div/div[2]/form/div[2]/input'

account_field = wait.until(
    EC.presence_of_element_located((By.XPATH, account_xpath))
)

account_field.clear()

# Fill in your account below (Kevinwu@7503)
account_field.send_keys('')

password_field = driver.find_element_by_xpath(password_xpath)

#Fill in your password below
password_field.send_keys("" + Keys.ENTER)

clockIO_btn_xpath = '//*[@id="omnibpm-main-menu"]/ul[3]/li[2]/button'

wait.until(
    EC.presence_of_element_located((By.XPATH, clockIO_btn_xpath))
).click()

clockin_btn_xpath = '//*[@id="mainui"]/div/div[1]/div[3]/div/div/div/div/div/div/button'
try:
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, clockin_btn_xpath))
    ).click()

except:
    print("Not the right time to clock in/out.")

time.sleep(2)
driver.quit()