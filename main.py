import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from field import Field
from model import Model

if __name__ == '__main__':
    driver = webdriver.Safari()
    driver.get(
        'https://108.181.33.119/__cpi.php?s=UkQ2YXlSaWJuc3ZoeGR2dG04WW9LaEJ0OHhrWnZuYXM1V3ViWENpeU9iRDdUNDc5NTdoMEphSGJaNHdGek1OU0tpc1p6M0FMNnB6eXhZSGdnSnNYczBvVmhCcU5ySC9aVkw5WE9WcVhPY2c9&r=aHR0cHM6Ly8xMDguMTgxLjMzLjExOS8%2FX19jcG89YUhSMGNITTZMeTkzZDNjdVlXMWhlbTl1TG1OdmJTNXRlQQ%3D%3D&__cpo=1/')

    search_box = WebDriverWait(driver, 20).until(
        ec.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )

    search_box.send_keys('Laptop')

    search_box.submit()

    raw_laptops = WebDriverWait(driver, 20).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-component-type=s-search-result]'))
    )

    laptop_fields = [
        Field('name', By.CSS_SELECTOR, '.a-text-normal'),
        Field('price', By.CSS_SELECTOR, '.a-price span'),
        Field('url', By.CSS_SELECTOR, 'a')
    ]

    laptops = [Model.from_element(laptop, laptop_fields) for laptop in raw_laptops]

    laptops_df = pd.DataFrame([laptop.get_fields() for laptop in laptops])

    laptops_df.to_excel('laptops.xlsx', index=False)
