from selenium import webdriver

from repositories.model_repository import ModelRepository
from web_scrapper import WebScrapper

if __name__ == '__main__':
    # driver = webdriver.Safari()
    # driver.get(
    #     'https://108.181.33.119/__cpi.php?s=UkQ2YXlSaWJuc3ZoeGR2dG04WW9LaEJ0OHhrWnZuYXM1V3ViWENpeU9iRDdUNDc5NTdoMEphSGJaNHdGek1OU0tpc1p6M0FMNnB6eXhZSGdnSnNYczBvVmhCcU5ySC9aVkw5WE9WcVhPY2c9&r=aHR0cHM6Ly8xMDguMTgxLjMzLjExOS8%2FX19jcG89YUhSMGNITTZMeTkzZDNjdVlXMWhlbTl1TG1OdmJTNXRlQQ%3D%3D&__cpo=1/')
    #
    # search_box = WebDriverWait(driver, 20).until(
    #     ec.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    # )
    #
    # search_box.send_keys('Laptop')
    #
    # search_box.submit()
    #
    # raw_laptops = WebDriverWait(driver, 20).until(
    #     ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-component-type=s-search-result]'))
    # )
    #
    # laptop_fields = [
    #     Field('name', By.CSS_SELECTOR, '.a-text-normal'),
    #     Field('price', By.CSS_SELECTOR, '.a-price span'),
    #     Field('url', By.CSS_SELECTOR, 'a')
    # ]
    #
    # laptops = [Model.from_element(laptop, laptop_fields) for laptop in raw_laptops]
    #
    # laptops_df = pd.DataFrame([laptop.get_fields() for laptop in laptops])
    #
    # laptops_df.to_excel('laptops.xlsx', index=False)

    driver = webdriver.Safari()
    model_repository = ModelRepository()

    raw_instructions = [
        {
            'action': 'navigate',
            'value': 'https://173.214.175.202/__cpi.php?s=UkQ2YXlSaWJuc3ZoeGR2dG04WW9LcTdZSHdzMXlBelY1emhPakRoWFFROC9lME5pQWZwZzMwU0FjdzZ3WmpwbTNIVU94dWc3S1A0L3ZUTmlFWTZYeDhCRUNWOUhZb05zcm9XNzJRZ0lWTVU9&r=aHR0cHM6Ly8xNzMuMjE0LjE3NS4yMDIvP19fY3BvPWFIUjBjSE02THk5M2QzY3VZVzFoZW05dUxtTnZiUzV0ZUE%3D&__cpo=1',
        },
        {
            'action': 'send keys',
            'by': 'id',
            'value': 'twotabsearchtextbox',
            'keys': 'Laptop'
        },
        {
            'action': 'submit',
            'by': 'id',
            'value': 'twotabsearchtextbox'
        },
        {
            'action': 'scrap models',
            'by': 'css selector',
            'model_name': 'laptops',
            'value': 'div[data-component-type=s-search-result]',
            'fields': [
                {
                    'name': 'name',
                    'by': 'css selector',
                    'value': '.a-text-normal'
                },
                {
                    'name': 'price',
                    'by': 'css selector',
                    'value': '.a-price span'
                },
                {
                    'name': 'url',
                    'by': 'css selector',
                    'value': 'a'
                }
            ],
        },
        {
            'action': 'to excel',
            'value': 'laptops.xlsx'
        }
    ]

    web_scrapper = WebScrapper(driver=driver, model_repository=model_repository)

    web_scrapper.fetch_instructions_from_directory('instructions')
    web_scrapper.run()
