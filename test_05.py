import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def prepare_faces():
    print("начало тестирования")
    browser = webdriver.Firefox()
    #return browser
    yield browser
    # этот код выполнится после завершения теста
    print("конец тестирования")
    time.sleep(5)
    browser.quit()








class TestPrintSmilingFaces():
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass
        # какие-то проверки
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_second_smiling_faces(self, prepare_faces):
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
        #x += 1
        #y += 1
        browser.close()
        
        # какие-то проверки
