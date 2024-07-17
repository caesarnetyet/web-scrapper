from selenium.webdriver.common.by import By


class Field:
    def __init__(self, name: str, by: By, value: str, default="N/A"):
        self.name = name
        self.by = by
        self.value = value
        self.default = default

    @staticmethod
    def from_json(json: dict):
        return Field(json['name'], json['by'], json['value'])
