class Dampen:
    def __init__(self):
        self.amount
        self.list = [16, 14, 12, 10, 8, 6, 4]

    def damp(self, thing, decrease=0):
        return thing / self.list(self.amount) - decrease

    def change(self):
        self.amount += 1
        if self.amount > 6:
            self.amount = 0
        print("dampen amount:", self.list(self.amount))
