import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestRouteSearch(unittest.TestCase):

    def setUp(self):
        # Укажите путь к вашему драйверу (например, ChromeDriver)
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.idos.cz/")  # Сайт IDOS

    def test_search_route(self):
        driver = self.driver
        # Найдите поле поиска и введите маршрут
        search_box = driver.find_element(By.ID, "search-input")
        search_box.send_keys("Praha - Brno")  # Введите маршрут
        search_box.send_keys(Keys.RETURN)     # Нажмите Enter

        time.sleep(3)  # Подождите, пока загрузится результат

        # Проверьте наличие результатов поиска
        results = driver.find_elements(By.CLASS_NAME, "result")
        self.assertTrue(len(results) > 0, "Поиск не дал результатов")

    def tearDown(self):
        # Закройте браузер после теста
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

