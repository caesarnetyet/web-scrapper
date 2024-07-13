from typing import List

import pandas as pd

from instruction import ScrapModelsInstruction, BaseInstruction


class ToExcelInstruction(BaseInstruction):
    def __init__(self, driver, value, models: List[ScrapModelsInstruction], timeout=20):
        super().__init__(driver, value)
        self.models = models
        self.timeout = timeout

    def execute(self):
        if not self.models:
            raise ValueError('No models to scrap')
        # join all the dataframes
        data = pd.concat([pd.DataFrame(model.scrap_models()) for model in self.models], ignore_index=True)
        data.to_excel(self.value, index=False)
