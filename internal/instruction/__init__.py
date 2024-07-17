from selenium.webdriver.chrome.webdriver import WebDriver

from internal.instruction.action import Action
from internal.instruction.base_instructions import BaseInstruction
from internal.instruction.click_instruction import ClickInstruction
from internal.instruction.navigate_instruction import NavigateInstruction
from internal.instruction.scrap_models__instruction import ScrapModelsInstruction
from internal.instruction.send_keys_instruction import SendKeysInstruction
from internal.instruction.submit_instruction import SubmitInstruction
from internal.instruction.to_excel_instruction import ToExcelInstruction


class Instruction(BaseInstruction):
    @staticmethod
    def from_dict(driver: WebDriver, data: dict, models_repository) -> 'BaseInstruction':
        try:
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
                    return ScrapModelsInstruction.from_json(driver, data, models_repository)
                case Action.TO_EXCEL:
                    return ToExcelInstruction(driver, data['value'], data['model_name'], models_repository)
                case _:
                    raise ValueError(f"Acción inválida: {data['action']}")
        except KeyError as e:
            raise ValueError(f"El campo {e} no fue encontrado.")
