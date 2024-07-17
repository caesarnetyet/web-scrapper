from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from internal.field import Field


class Model:
    _fields: list[Field]
    _source: WebElement

    def __init__(self, source: WebElement, fields=None):
        if fields is None:
            fields = []
        self.source = source
        self._fields = fields

    @staticmethod
    def from_driver(driver: WebDriver, by: By, value: str, timeout=20):
        source = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((str(by), value))
        )
        return Model(source)

    @staticmethod
    def from_driver_with_fields(driver: WebDriver, by: By, value: str, fields: list[Field], timeout=20):
        source = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((str(by), value))
        )
        return Model(source, fields)

    @staticmethod
    def from_element(element: WebElement, fields: list[Field]):
        return Model(element, fields)

    def add_fields(self, fields: list[Field]):
        self._fields = fields

    def get_field_value(self, field: Field):
        try:
            if field.value == 'a':
                return self.source.find_element(field.by, field.value).get_attribute('href')
            return self.source.find_element(field.by, field.value).text
        except Exception:
            return field.default

    def get_fields(self):
        return {field.name: self.get_field_value(field) for field in self._fields}

    def __str__(self):
        return str(self.get_fields())
