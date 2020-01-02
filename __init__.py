from mycroft import MycroftSkill, intent_file_handler


class IkeaTradfri(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tradfri.ikea.intent')
    def handle_tradfri_ikea(self, message):
        self.speak_dialog('tradfri.ikea')


def create_skill():
    return IkeaTradfri()

