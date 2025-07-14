import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time
import pyautogui

if __name__ == "__main__":
    load_dotenv()

    form_link = os.getenv("FORM_LINK")
    driver = uc.Chrome()

    driver.get(form_link)
    driver.maximize_window()
    time.sleep(5)
    pyautogui.click(673, 525)
    print("Clicked!")
    driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div").click()
    print("Clicked next!")
    time.sleep(5)