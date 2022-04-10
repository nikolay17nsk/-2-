from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time




@pytest.fixture(autouse=True)
def browser():
    print("начало тестирования")
    browser = webdriver.Firefox()
    yield browser
    # этот код выполнится после завершения теста
    print("конец тестирования")
    time.sleep(5)
    browser.quit()

class TestAbs():
    
    
        
    def test_abs1(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        x = 0
        y = 0
        
        browser = webdriver.Firefox()
        browser.get("http://suninjuly.github.io/registration1.html")
        se1 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.first_class > input")
        se1.send_keys("NIKOLAY")
        se2 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.second_class > input")
        se2.send_keys("NIKOLAY")
        se3 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.third_class > input")
        se3.send_keys("NIKOLAY")
        
        #self.assertEqual(x, 1, "я хз что должно произойти")
        se4 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.second_block > div.form-group.first_class > input")
        se4.send_keys("NIKOLAY")
        se5 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.second_block > div.form-group.second_class > input")
        se5.send_keys("NIKOLAY")
        se6 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > button").click()
        x += 1
        y += 1
        browser.close()
        #self.assertEqual(x, 1, "я хз что должно произойти")
            
    def test_abs2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time
        
        x = 0
        browser = webdriver.Firefox()
        browser.get("http://suninjuly.github.io/registration2.html")
        time.sleep(3)
        se1 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.first_class > input")
        se1.send_keys("NIKOLAY")
        se2 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.first_block > div.form-group.third_class > input")
        se2.send_keys("NIKOLAY")
        se3 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.second_block > div.form-group.first_class > input")
        se3.send_keys("NIKOLAY")
        
        #self.assertEqual(x, 1, "я хз что должно произойти")
        se4 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div.second_block > div.form-group.second_class > input")
        se4.send_keys("NIKOLAY")
        se5 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > button").click()
        x += 1
        time.sleep(15)
        browser.close()
        
        
        
        #self.assertEqual(x, 1, "я хз что должно произойти")
        

