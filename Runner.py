#!/usr/bin/env python3

from Benchmark import Benchmark
import sys


def run_solver():
    if len(sys.argv) > 1 and sys.argv[1] and sys.argv[2]:
        assert int(sys.argv[1]) > 0 and int(sys.argv[1]) not in [0, 2, 3]
        assert int(sys.argv[2]) > 1
        b = Benchmark(int(sys.argv[1]), int(sys.argv[2]))
        b.run()
    else:
        n = int(input("Please insert the number of queens: "))
        it = int(input("Please insert the number of iterations: "))
        assert it > 1
        assert n > 0 and n not in [0, 2, 3]
        b = Benchmark(n, it)
        b.run()
    

if __name__ == '__main__':
    run_solver()
