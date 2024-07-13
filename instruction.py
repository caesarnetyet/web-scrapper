from selenium.webdriver.common.by import By


class Instruction:
    def __init__(self, driver, by: By, value: str, action: Action):
        self.driver = driver
        self.by = by
        self.value = value
        self.action = action

    def execute(self):
        match self.action:
            case Action.CLICK:
                element = self.driver.find_element(self.by, self.value)
                element.click()
            case Action.SEND_KEYS:
                element = self.driver.find_element(self.by, self.value)
                element.send_keys(self.value)
            case Action.SUBMIT:
                element = self.driver.find_element(self.by, self.value)
                element.submit()
            case Action.NAVIGATE:
                self.driver.get(self.value)
            case Action.GET_MODELS:
                elements = self.driver.find_elements(self.by, self.value)
                return elements
            case Action.ADD_FIELD:
                element = self.driver.find_element(self.by, self.value)
                return element
            case Action.TO_EXCEL:
                return self.value
            case _:
                raise NotImplementedError(f'{self.action} is not implemented')
