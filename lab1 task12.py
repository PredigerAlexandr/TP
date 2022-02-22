class Summator:
    def transform(self, n):
        return n

    def Sum(self, n):
        count = 0
        for i in range(n + 1):
            count += self.transform(i)
        return count


class PowerSummator(Summator):
    def __init__(self, degree=1):
        self.degree = degree

    def transform(self, n):
        return n ** self.degree


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)




class CubSummator(PowerSummator, Summator):
    def __init__(self, degree=3):
        PowerSummator.__init__(self, degree)
        Summator.__init__(self)
        self.degree = degree


summator = PowerSummator(10)
per = summator.Sum(5)
print(per)
squareSummator = SquareSummator()
per = squareSummator.Sum(3)
print(per)
cubSummator = CubSummator()
per = cubSummator.Sum(3)
print(per)
