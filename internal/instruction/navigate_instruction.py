from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from internal.instruction import BaseInstruction


class NavigateInstruction(BaseInstruction):
    proxyProvider = "https://www.croxyproxy.com/"

    def __init__(self, driver: WebDriver, value: str, with_proxy=False):
        super().__init__(driver, value)
        self.with_proxy = with_proxy

    def execute(self):
        if self.with_proxy:
            self.execute_with_proxy()
        else:
            self.driver.get(self.value)

    def execute_with_proxy(self):
        self.driver.get(self.proxyProvider)
        input_ = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.ID, "url"))
        )
        input_.send_keys(self.value)
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.ID, "requestSubmit"))
        ).click()
