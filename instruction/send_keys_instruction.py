from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from instruction import Instruction


class SendKeysInstruction(Instruction):
    def __init__(self, driver, value, by: By, keys: str, timeout=20):
        super().__init__(driver, value)
        self.by = by
        self.keys = keys
        self.timeout = timeout

    def execute(self):
        WebDriverWait(self.driver, self.timeout).until(
            ec.element_to_be_clickable((str(self.by), self.value))
        ).send_keys(self.keys)
