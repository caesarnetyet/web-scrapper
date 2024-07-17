import pandas as pd

from internal.instruction import BaseInstruction
from repositories.model_repository import ModelRepository


class ToExcelInstruction(BaseInstruction):
    def __init__(self, driver, value, model_name: str, model_repository: ModelRepository):
        super().__init__(driver, value)
        self.model_repository = model_repository
        self.model_name = model_name

    def execute(self):
        model = self.model_repository.get_models_by_name(self.model_name)
        df = pd.DataFrame(model)
        df.to_excel(f"output/{self.model_name}.xlsx", index=False)
