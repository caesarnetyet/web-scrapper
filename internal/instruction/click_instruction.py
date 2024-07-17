from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from internal.instruction import BaseInstruction


class ClickInstruction(BaseInstruction):
    def __init__(self, driver, value, by: By, timeout=20):
        super().__init__(driver, value)
        self.by = by
        self.timeout = timeout

    def execute(self):
        WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable((str(self.by), self.value))
        ).click()
