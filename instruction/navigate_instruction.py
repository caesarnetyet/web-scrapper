from selenium.webdriver.chrome.webdriver import WebDriver

from instruction import Instruction


class NavigateInstruction(Instruction):
    def __init__(self, direction, driver: WebDriver, value: str):
        super().__init__(driver, value)
        self.direction = direction

    def execute(self):
        self.driver.get(self.value)
