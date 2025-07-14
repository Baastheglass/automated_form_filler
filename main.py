import undetected_chromedriver as uc
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    form_link = os.getenv("FORM_LINK")
    driver = uc.Chrome()

    driver.get(form_link)