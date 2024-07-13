from typing import List

from selenium.webdriver.chrome.webdriver import WebDriver

from instruction.action import Action
from instruction.base_instructions import BaseInstruction
from instruction.click_instruction import ClickInstruction
from instruction.navigate_instruction import NavigateInstruction
from instruction.scrap_models__instruction import ScrapModelsInstruction
from instruction.send_keys_instruction import SendKeysInstruction
from instruction.submit_instruction import SubmitInstruction
from instruction.to_excel_instruction import ToExcelInstruction


class Instruction(BaseInstruction):
    @staticmethod
    def from_dict(driver: WebDriver, data: dict, models: List[ScrapModelsInstruction] = None) -> 'BaseInstruction':
        if models is None:
            models = []

        match Action(data['action']):
            case Action.SEND_KEYS:
                return SendKeysInstruction(driver, data['value'], data['by'], data['keys'])
            case Action.SUBMIT:
                return SubmitInstruction(driver, data['value'], data['by'])
            case Action.NAVIGATE:
                return NavigateInstruction(driver, data['value'])
            case Action.CLICK:
                return ClickInstruction(driver, data['value'], data['by'])
            case Action.SCRAP_MODELS:
                return ScrapModelsInstruction.from_json(driver, data)
            case Action.TO_EXCEL:
                return ToExcelInstruction(driver, data['value'], models)
            case _:
                raise ValueError(f"Acción inválida: {data['action']}")
