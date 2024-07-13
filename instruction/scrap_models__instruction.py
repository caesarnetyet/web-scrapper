from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from field import Field
from instruction import BaseInstruction
from model import Model


class ScrapModelsInstruction(BaseInstruction):
    raw_models: List[WebElement]

    def __init__(self, driver, by: By, value: str, fields: List[Field], model_name: str, timeout=20):
        super().__init__(driver, value)
        self.by = by
        self.fields = fields
        self.model_name = model_name
        self.timeout = timeout

    @staticmethod
    def from_json(driver, json):
        by = json['by']
        value = json['value']
        fields = [Field.from_json(field) for field in json['fields']]
        model_name = json['model_name']
        timeout = json.get('timeout', 20)
        return ScrapModelsInstruction(driver, by, value, fields, model_name, timeout)

    def execute(self):
        self.raw_models = WebDriverWait(self.driver, self.timeout).until(
            ec.presence_of_all_elements_located((str(self.by), self.value))
        )

    def scrap_model(self, web_element: WebElement):
        model = Model.from_element(web_element, self.fields)
        return model.get_fields()

    def scrap_models(self):
        return [self.scrap_model(raw_model) for raw_model in self.raw_models]
