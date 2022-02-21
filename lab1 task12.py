class Summator:
    def __init__(self, N=0, count=0, degree = 1):
        self.N = N
        self.count = count;
        self.degree = degree

    def transform(self, n):
        return n ** self.degree

    def Sum(self, n):
        for i in range(n + 1):
            self.count += self.transform(i)
        return self.count


class PowerSummator(Summator):
    def __init__(self, degree=0):
        super().__init__(self)
        self.degree = degree

    def transform(self, n):
        return n ** self.degree

    def Sum(self, n):
        for i in range(n + 1):
            self.count += self.transform(i)
        return self.count


class SquareSummator(PowerSummator, Summator):
    def __init__(self, degree=2):
        PowerSummator.__init__(self, degree)
        Summator.__init__(self)
        self.degree = degree


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
