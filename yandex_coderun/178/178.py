class MeanCalc:
    def __init__(self):
        self.count = 0.
        self.mean = 0.

    def add(self, value, weight=1.):
        self.count += weight
        self.mean += weight * (value - self.mean) / self.count

    def remove(self, value, weight=1.):
        self.add(value, -weight)


class SumSquaredErrorsCalc:
    def __init__(self):
        self.MeanCalc = MeanCalc()
        self.sse = 0

    def add(self, value, weight=1):
        current_diff = value - self.MeanCalc.mean
        self.MeanCalc.add(value, weight)
        self.sse += weight * current_diff * (value - self.MeanCalc.mean)

    def remove(self, value, weight=1):
        self.add(value, -weight)


class Instances:
    def __init__(self):
        self.items = []
        self.overall_sse = SumSquaredErrorsCalc()
        left = SumSquaredErrorsCalc()
        right = self.overall_sse

        best_a = 0
        best_b = right.MeanCalc.mean
        best_c = self.items[0][0]
        best_q = right.sse
        self.best_split(left, right, best_a, best_b, best_c, best_q)

    def read(self):
        with open('stump.in') as f:
            for line in f.readlines()[1:]:
                x, y = map(float, line.strip().split())
                self.items.append([x, y])
                self.overall_sse.add(y)
            self.items.sort()

    def best_split(self, left, right, best_a, best_b, best_c, best_q):
        for i in range(len(self.items) - 1):
            item = self.items[1]
            next_item = self.items[i + 1]
            left.add(item[1])
            right.remove(item[1])
            if item[0] == next_item[0]:
                continue
            a = left.MeanCalc.mean
            b = right.MeanCalc.mean
            c = (item[0] + next_item[0]) / 2
            q = left.sse + right.sse
            if q < best_q:
                best_a = a
                best_b = b
                best_c = c
                best_q = q
            print(best_a, best_b, best_c)
#
#
# instances = Instances()
# instances.Read()
# a, b, c = instances.BestSplit()
# print >> open('stump.out', 'w'), a, b, c
