from collections import defaultdict

class Factorizer:
    def __init__(self, n):
        self.n = n
    
    def compute_factors(self, l):
        for n in l:    
            if n > 15:
                for i in range (n-1, 3, -1):
                    if not n % i and n // i not in (0, 1, 2, 3):
                        l.append(i)
                        l.append(n // i)
                        l.remove(n)
                        return True
        return False

    def factorize(self):
        res = [self.n]
        while self.compute_factors(res):
            self.compute_factors(res)
        d = defaultdict(int)
        for i in res:
            d[i] += 1
        return d
