from _thread import start_new_thread

class Event:

    def __init__(self):
        pass
        self.events = {}

    def init(self):
        self.events.update({"": ""})
        self.events.update({"": ""})
        self.events.update({"": ""})

    def create(self, name):
        self.events.update({name: ""})

    def call(self, name):
        pass
