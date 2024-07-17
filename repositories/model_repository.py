from typing import List

from internal.model import Model


class ModelRepository:
    _models_datasource = {}

    def __init__(self):
        pass

    def add_models(self, model_name: str, new_models: List[Model]):
        print(new_models)
        if model_name not in self._models_datasource:
            self._models_datasource[model_name] = []

        self._models_datasource[model_name].extend(new_models)

    def get_models_by_name(self, model_name: str) -> List[Model]:
        return self._models_datasource.get(model_name, [])

    def clear_models(self, model_name: str):
        self._models_datasource[model_name] = []

    def clear_all_models(self):
        self._models_datasource = {}