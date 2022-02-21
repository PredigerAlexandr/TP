class Summator:
    def __init__(self, N=0, count=0):
        self.N = N
        self.count = count;

    def transform(self, n):
        return n

    def Sum(self, n):
        for i in range(n + 1):
            self.count += self.transform(i)
        return self.count


class SquareSummator(Summator):
    def __init__(self, N=0, count=0):
        super().__init__(N, count)

    def transform(self, n):
        return n**2

    def Sum(self, n):
        for i in range(n + 1):
            self.count += self.transform(i)
        return self.count

class CubSummator(Summator):
    def __init__(self, N=0, count=0):
        super().__init__(N, count)

    def transform(self, n):
        return n**3

    def Sum(self, n):
        for i in range(n + 1):
            self.count += self.transform(i)
        return self.count


summator = Summator()
per = summator.Sum(3)
print(per)
squareSummator = SquareSummator()
per = squareSummator.Sum(3)
print(per)
cubSummator = CubSummator()
per = cubSummator.Sum(3)
print(per)