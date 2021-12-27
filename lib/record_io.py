class RecordIO():
    
    """RecordIO class
    
    Ask user for training data.

    """

    def __init__(self):
        self.input_buffer = {}
    
    def ask_save_multi(self, names):
        for name in names:
            self.ask(name)
            self.get_and_save(name)

    def ask(self, name):
        print("Enter {0}:".format(name.capitalize()))
    
    def get_and_clear_buffer(self):
        ret = self.input_buffer
        self.input_buffer = {}

        return ret
    
    def get_and_save(self, name):
        self.input_buffer[name.lower()] = input()
    
    def show(self):
        for name, value in self.input_buffer.items():
            print("{0}: {1}".format(name.capitalize(), value))
    
    def clear(self):
        self.input_buffer = {}
