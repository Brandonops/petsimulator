class Treat:
    def __init__(self, satiate = 10, fun = 10):
        self.satiate = satiate
        self.fun = fun
        
class ColdPizza(Treat):
    def __init__(self):
        super().__init__(15, 20)

class Bacon(Treat):
    def __init__(self):
        super().__init__(30, 30)

class VeganSnack(Treat):
    def __init__(self):
        super().__init__(2, -2)