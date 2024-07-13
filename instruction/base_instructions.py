from selenium.webdriver.chrome.webdriver import WebDriver


class BaseInstruction:
    def __init__(self, driver: WebDriver, value: str):
        self.driver = driver
        self.value = value

    def execute(self):
        pass
