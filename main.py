from time import sleep
from selenium import webdriver

from settings import USER_DATA_DIR, PROFILE_DIRECTORY

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={USER_DATA_DIR}")
    options.add_argument(f"--profile-directory={PROFILE_DIRECTORY}")
    return webdriver.Chrome("./chromedriver", options=options)

def go_to_whatsapp(driver):
    driver.get("https://web.whatsapp.com/")

def archive_chats(driver):
    chats = driver.find_elements_by_class_name("_2WP9Q")
    for chat in chats:
        chat.click()
        sleep(1)
        driver.find_element_by_xpath("//span[@data-icon='down']").click()
        sleep(1)
        driver.find_element_by_xpath("//div[@title='Archive chat']").click()
        sleep(1)

driver = init_driver()

try:
    go_to_whatsapp(driver)
    sleep(10)
    archive_chats(driver)
except:
    pass

sleep(5)
driver.close()
