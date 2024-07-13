from selenium.webdriver.chrome.webdriver import WebDriver

from instruction import BaseInstruction


class NavigateInstruction(BaseInstruction):
    def __init__(self, driver: WebDriver, value: str):
        super().__init__(driver, value)

    def execute(self):
        self.driver.get(self.value)
