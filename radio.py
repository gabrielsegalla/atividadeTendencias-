import random

class Radio:

    status = False
    history_status = []
    frequency = 0
    history_frequency = []

    def get_status(self):
        return self.status

    def set_status(self):
        self.status = not self.status
        self.history_status.append(self.status)
        print(self.status)
        print(self.history_status)
        return self.get_status
    
    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        if self.status == True:
            self.frequency = frequency
            self.history_frequency.append(self.frequency)
            return self.frequency

    def set_next_frequency(self):
        if self.status == True:
            frequency = random.randint(self.frequency, self.frequency + 15)
            for f in range(frequency):
                self.set_frequency(f)

    def set_previous_frequency(self):
        if self.status == True:
            frequency = random.randint(self.frequency -15, self.frequency)
            # import ipdb; ipdb.set_trace()
            for f in range(self.frequency, frequency, -1):
                self.set_frequency(f)
