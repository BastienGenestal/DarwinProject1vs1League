import math

class EloCalculation:
    def __init__(self, eloA, eloB):
        self.eloA = eloA
        self.eloB = eloB
        self.K = 30
        self.Pb = self.prob(eloA, eloB)
        self.Pa = self.prob(eloB, eloA)

    @staticmethod
    def prob(a, b):
        return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (a - b) / 400))

    def calculate(self, d):
        if d == 1:
            Ra = self.eloA + self.K * (1 - self.Pa)
            Rb = self.eloB + self.K * (0 - self.Pb)
        else:
            Ra = self.eloA + self.K * (0 - self.Pa)
            Rb = self.eloB + self.K * (1 - self.Pb)
        return round(Ra), round(Rb)