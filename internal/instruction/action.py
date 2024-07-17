from enum import Enum


class Action(Enum):
    CLICK = 'click'
    SEND_KEYS = 'send keys'
    SUBMIT = 'submit'
    NAVIGATE = 'navigate'
    SCRAP_MODELS = 'scrap models'
    ADD_FIELD = 'add field'
    TO_EXCEL = 'to excel'
