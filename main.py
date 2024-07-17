import platform

from selenium import webdriver

from repositories.model_repository import ModelRepository
from web_scrapper import WebScrapper


def get_driver():
    driver_: webdriver
    match platform.system():
        case 'Windows':
            driver_ = webdriver.Edge()
        case 'Linux':
            driver_ = webdriver.Chrome()
        case _:
            driver_ = webdriver.Safari()
    return driver_


if __name__ == '__main__':
    driver = get_driver()

    model_repository = ModelRepository()
    web_scrapper = WebScrapper(driver=driver, model_repository=model_repository)

    web_scrapper.fetch_instructions_from_directory('instructions')
    web_scrapper.run()
