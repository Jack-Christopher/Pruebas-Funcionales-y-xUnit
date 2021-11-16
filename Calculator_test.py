import unittest
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#define the configuration for the test
s = Service(EdgeChromiumDriverManager("latest", cache_valid_range=1, log_level=0).install())
driver = webdriver.Edge(service=s)


def WebPercentageCalculator(a,b):
    driver.find_element(by=By.XPATH, value="//*[@id='cpar1']").send_keys(a)
    driver.find_element(by=By.XPATH, value="//*[@id='cpar2']").send_keys(b)
    driver.find_element(by=By.XPATH, value="//*[@id='content']/table/tbody/tr[2]/td/input[2]").click()
    result = driver.find_element(by=By.XPATH, value="//*[@id='content']/p[2]/font/b").text
    return float(result)

def Percentage(a,b):
    return (a*b)/100



class TestWebPercentageCalculator(unittest.TestCase):
    def setUp(self) -> None:
        driver.get("https://www.calculator.net/percent-calculator.html")
        return super().setUp()

    def test_data_between_0_and_100(self):
        # Porcentaje dentro del rango de 0 a 100
        a = randint(1, 99)
        b = randint(1, 99)
        self.assertEqual(WebPercentageCalculator(a,b), Percentage(a,b))
            

    def test_percentage_0(self):
        # Porcentaje 0    
        b = randint(0, 100)
        self.assertEqual(WebPercentageCalculator(0,b), Percentage(0,b))
        
    
    def test_percentage_100(self):
        # Porcentaje 100
        b = randint(0, 100)
        self.assertEqual(WebPercentageCalculator(100,b), Percentage(100,b))
            

    def test_percentage_greater_than_100(self):
        # Porcentaje mayor a 100
        a = randint(101, 1000)
        b = randint(0, 1000)
        self.assertEqual(WebPercentageCalculator(a,b), Percentage(a,b))
        

    def test_percentage_less_than_0(self):
        # Porcentaje menor a 0
        a = randint(-1000, -1)
        b = randint(0, 1000)
        self.assertEqual(WebPercentageCalculator(a,b), Percentage(a,b))
        
    
    def test_negative_number(self):
        # Numero negativo
        a = randint(0, 100)
        b = randint(-1000, -1)
        self.assertEqual(WebPercentageCalculator(a,b), Percentage(a,b))    
        

    def test_number_zero(self):
        # Numero 0
        a = randint(0, 100)
        self.assertEqual(WebPercentageCalculator(a,0), Percentage(a,0))


if __name__ == '__main__':
    unittest.main()


driver.quit() # close all tabs
