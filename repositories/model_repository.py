from typing import List


class ModelRepository:
    _models: List[dict] = []

    def __init__(self):
        pass

    def add_models(self, name, model: List[dict]):
        self._models.append({name: model})

    def get_models_by_name(self, name: str):
        return [model[name] for model in self._models]

    def get_models(self):
        return self._models

    def clear(self):
        self._models = []
