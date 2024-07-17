from selenium import webdriver

from repositories.model_repository import ModelRepository
from web_scrapper import WebScrapper

if __name__ == '__main__':
    driver = webdriver.Edge()
    model_repository = ModelRepository()

    web_scrapper = WebScrapper(driver=driver, model_repository=model_repository)

    web_scrapper.fetch_instructions_from_directory('instructions')
    web_scrapper.run()
