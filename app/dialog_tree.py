import json
from pprint import pprint

class DialogTree:
    data = None
    __current_state = 'intro'

    def load(self, filename='dialog.json'):
        with open(filename) as data_source:
            self.data = json.load(data_source)

    def select_option(self, option):
            self.__current_state = self.current_state['options'][option - 1]['state']

    @property
    def current_state(self):
        return self.data['states'][self.__current_state]

    @property
    def active_text(self):
        index = 1
        output = self.current_state['text']

        for option in self.current_state['options']:
            output += ". {0}, press {1}".format(option['text'], index)
            index += 1

        output += ". To hear these options again, press 9"
        output += ". To speak to an operator, press 0."

        return output
