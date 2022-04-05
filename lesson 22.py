from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 13).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "$100"))
    )
se1 = browser.find_element(By.CSS_SELECTOR, "#book").click()
