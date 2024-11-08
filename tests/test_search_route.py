import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestRouteSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://idos.cz/")
        self.driver.maximize_window()
        time.sleep(2)  # Дать время для загрузки страницы

    def test_search_route(self):
        driver = self.driver

        # Подтверждение согласия с cookies
        try:
            consent_button = driver.find_element(By.ID, "didomi-notice-agree-button")
            consent_button.click()
            time.sleep(2)
        except:
            print("Кнопка согласия с cookies не найдена.")

        # Пример для начальной точки "Откуда"
        start_button = driver.find_element(By.XPATH, '//*[@id="From"]')
        start_button.click()
        start_button.send_keys("Praha")  # Введите начальный пункт

        # Пример для конечной точки "Куда"
        end_button = driver.find_element(By.XPATH, '//*[@id="To"]')
        end_button.click()
        end_button.send_keys("Brno")  # Введите конечный пункт

        # Нажмите Enter для поиска
        end_button.send_keys(Keys.RETURN)
        time.sleep(3)  # Подождите, пока загрузится результат

        # Проверка наличия результатов поиска
        results = driver.find_elements(By.ID, "col-content")
        self.assertGreater(len(results), 0, "Результаты поиска не найдены.")

        # Вывод сообщения об успешном прохождении теста
        print("Тест успешно пройден: результаты поиска отображены.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
