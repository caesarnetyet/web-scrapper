from selenium.webdriver.chrome.webdriver import WebDriver

from instruction.action import Action
from instruction.click_instruction import ClickInstruction
from instruction.navigate_instruction import NavigateInstruction
from instruction.scrap_models__instruction import ScrapModelsInstruction
from instruction.send_keys_instruction import SendKeysInstruction
from instruction.submit_instruction import SubmitInstruction


class Instruction:
    def __init__(self, driver: WebDriver, value: str):
        self.driver = driver
        self.value = value

    @staticmethod
    def from_dict(driver: WebDriver, data: dict) -> 'Instruction':
        match Action(data['action']):
            case Action.SEND_KEYS:
                return SendKeysInstruction(driver, data['value'], data['by'], data['keys'])
            case Action.SUBMIT:
                return SubmitInstruction(driver, data['value'], data['by'])
            case Action.NAVIGATE:
                return NavigateInstruction(data['direction'], driver, data['value'])
            case Action.CLICK:
                return ClickInstruction(driver, data['value'], data['by'])
            case Action.SCRAP_MODELS:
                return ScrapModelsInstruction(driver, data['value'])
            case _:
                raise ValueError(f"Invalid action: {data['action']}")

    def execute(self):
        pass
