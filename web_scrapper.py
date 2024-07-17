import json
import os
from typing import List

from internal.instruction import Instruction, BaseInstruction


class WebScrapper:
    def __init__(self, model_repository, driver):
        self.model_repository = model_repository
        self.driver = driver
        self.instructions: List[BaseInstruction] = []

    def fetch_instructions_from_directory(self, directory: str):
        files = [f for f in os.listdir(directory) if os.path.isfile(f"{directory}/{f}")]

        for file in files:
            print("Cargando archivo", file)
            with open(f"{directory}/{file}") as f:
                instructions: dict = json.load(f)
                self.instructions.extend(
                    [Instruction.from_dict(self.driver, instruction, self.model_repository) for instruction in
                     instructions])

    def run(self):
        if not self.instructions:
            raise ValueError("No hay instrucciones para ejecutar")
        for instruction in self.instructions:
            instruction.execute()
