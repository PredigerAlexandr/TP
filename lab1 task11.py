class Summator:
    def __init__(self, N=0):
        self.N = N

    def transform(self, n):
        return n

    def Sum(self, n):
        count = 0
        for i in range(n + 1):
            count += self.transform(i)
        return count


class SquareSummator(Summator):
    def __init__(self, N=0):
        super().__init__(N)

    def transform(self, n):
        return n**2

class CubSummator(Summator):
    def __init__(self, N=0):
        super().__init__(N)

    def transform(self, n):
        return n**3


summator = Summator()
per = summator.Sum(3)
print(per)
squareSummator = SquareSummator()
per = squareSummator.Sum(3)
print(per)
cubSummator = CubSummator()
per = cubSummator.Sum(3)
print(per)