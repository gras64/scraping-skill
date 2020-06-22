from mycroft import MycroftSkill, intent_file_handler


class Scraping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('scraping.intent')
    def handle_scraping(self, message):
        self.speak_dialog('scraping')


def create_skill():
    return Scraping()

