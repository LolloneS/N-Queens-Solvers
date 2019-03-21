#!/usr/bin/env python3

from time import time
from ConstraintPropagationSolver import ConstraintPropagationSolver
from LocalSearchSolver import LocalSearchSolver
from GlobalSearchSolver import GlobalSearchSolver
from Kronecker import Kronecker

class Benchmark:
    def run_cpb(self):
        times = []
        steps = []
        for i in range(self.iterations):
            starting_time = time()
            s1 = ConstraintPropagationSolver(self.queens)
            s1.solve()
            times.append(time() - starting_time)
            steps.append(s1.count)
        
        m = round(sum(times) / self.iterations, 3)
        var = sum([(i - m)**2 for i in times]) / (self.iterations - 1)
        var_steps = sum([(i - m)**2 for i in steps]) / (self.iterations - 1)

        print("\nCPB BENCHMARK: queens = {}, iterations = {}\n".format(self.queens,self.iterations))
        print("Total time required " + str(round(sum(times), 2)) + " seconds")
        print("Average time required: " + str(m) + " seconds")
        print("Time taken by the worst iteration: " + str(round(max(times), 2)) + " seconds")
        print("Standard deviation (corrected) of the results " + str(round(var**0.5, 2)) + " seconds")
        times.remove(max(times))
        print("Average time required not considering the worst iteration: " + str(round(sum(times)/(self.iterations-1), 3)) + " seconds")
        
        print("Total steps: " + str(sum(steps)))
        print("Average steps required: " + str(sum(steps)/self.iterations))
        print("Steps taken by the worst iteration: " + str(max(steps)))
        print("Standard deviation (corrected) of the steps " + str(round(var_steps**0.5, 2)) + " steps")
        steps.remove(max(steps))
        print("Average steps required not considering the worst iteration: " + str(round(sum(steps)/(self.iterations-1), 3)) + " steps")


    def run_local(self):
        times = []
        solutions = []
        steps = []
        for i in range(self.iterations):
            starting_time = time()
            s1 = LocalSearchSolver(self.queens)
            sol1 = s1.solve()
            times.append(time() - starting_time)
            if sol1.is_a_solution():
                solutions.append(1)
            else:
                solutions.append(0)   
            steps.append(s1.count) 
        

        m = round(sum(times) / self.iterations, 3)
        var = sum([(i - m)**2 for i in times]) / (self.iterations - 1)
        var_steps = sum([(i - m)**2 for i in steps]) / (self.iterations - 1)

        print("\nLOCAL SEARCH BENCHMARK: queens = {}, iterations = {}\n".format(self.queens,self.iterations))
        print("Total time required " + str(round(sum(times), 2)) + " seconds")
        print("Average time required: " + str(m) + " seconds")
        print("Time taken by the worst iteration: " + str(round(max(times), 2)) + " seconds")
        print("Number of actual solutions = {} out of {}  ({}%)".format(sum(solutions), self.iterations, round(sum(solutions)/self.iterations * 100, 2)))
        print("Standard deviation (corrected) of the results " + str(round(var**0.5, 2)) + " seconds")
        times.remove(max(times))
        print("Average time required not considering the worst iteration: " + str(round(sum(times)/(self.iterations-1), 3)) + " seconds")

        print("Total steps: " + str(sum(steps)))
        print("Average steps required: " + str(sum(steps)/self.iterations))
        print("Steps taken by the worst iteration: " + str(max(steps)))
        print("Standard deviation (corrected) of the steps " + str(round(var_steps**0.5, 2)) + " steps")
        steps.remove(max(steps))
        print("Average steps required not considering the worst iteration: " + str(round(sum(steps)/(self.iterations-1), 3)) + " steps")




    def run_global(self):
        times = []
        steps = []
        for i in range(self.iterations):
            starting_time = time()
            s1 = GlobalSearchSolver(self.queens)
            sol1 = s1.solve()
            times.append(time() - starting_time)
            steps.append(s1.count)
        
        m = round(sum(times) / self.iterations, 3)
        var = sum([(i - m)**2 for i in times]) / (self.iterations - 1)
        var_steps = sum([(i - m)**2 for i in steps]) / (self.iterations - 1)

        print("\nGLOBAL SEARCH BENCHMARK: queens = {}, iterations = {}\n".format(self.queens,self.iterations))
        print("Total time required " + str(round(sum(times), 2)) + " seconds")
        print("Average time required: " + str(m) + " seconds")
        print("Time taken by the worst iteration: " + str(round(max(times), 2)) + " seconds")
        print("Standard deviation (corrected) of the results " + str(round(var**0.5, 2)) + " seconds")
        times.remove(max(times))
        print("Average time required not considering the worst iteration: " + str(round(sum(times)/(self.iterations-1), 3)) + " seconds")

        print("Total steps: " + str(sum(steps)))
        print("Average steps required: " + str(sum(steps)/self.iterations))
        print("Steps taken by the worst iteration: " + str(max(steps)))
        print("Standard deviation (corrected) of the steps " + str(round(var_steps**0.5, 2)) + " steps")
        steps.remove(max(steps))
        print("Average steps required not considering the worst iteration: " + str(round(sum(steps)/(self.iterations-1), 3)) + " steps")




    def run_kronecker(self, method="GS"):
        times = []
        solutions = []

        for i in range(self.iterations):
            starting_time = time()
            s1 = Kronecker(self.queens, method)
            sol1 = s1.solve()
            times.append(time() - starting_time)
            if sol1.is_a_solution():
                solutions.append(1)
            else:
                solutions.append(0)    
        
        m = round(sum(times) / self.iterations, 3)
        var = sum([(i - m)**2 for i in times]) / (self.iterations - 1)
        
        print("\nKRONECKER BENCHMARK ({}): queens = {}, iterations = {}\n".format(method, self.queens,self.iterations))
        print("Total time required " + str(round(sum(times), 2)) + " seconds")
        print("Average time required: " + str(m) + " seconds")
        print("Time taken by the worst iteration: " + str(round(max(times), 2)) + " seconds")
        print("Number of actual solutions = {} out of {}  ({}%)".format(sum(solutions), self.iterations, round(sum(solutions)/self.iterations * 100, 2)))
        print("Standard deviation (corrected) of the results " + str(round(var**0.5, 2)) + " seconds")
        times.remove(max(times))
        print("Average time required not considering the worst iteration: " + str(round(sum(times)/(self.iterations-1), 3)) + " seconds")

    
    def run_gs_from_kron(self):
        times = []
        for i in range(self.iterations):
            starting_time = time()
            s1 = Kronecker(self.queens, 'GS')
            sol1 = s1.solve()
            s2 = GlobalSearchSolver(sol1).solve()
            times.append(time() - starting_time)

        m = round(sum(times) / self.iterations, 3)
        var = sum([(i - m)**2 for i in times]) / (self.iterations - 1)
            
        print("\nGLOBAL SEARCH FROM KRON BENCHMARK: queens = {}, iterations = {}\n".format(self.queens,self.iterations))
        print("Total time required " + str(round(sum(times), 2)) + " seconds")
        print("Average time required: " + str(m) + " seconds")
        print("Time taken by the worst iteration: " + str(round(max(times), 2)) + " seconds")
        print("Standard deviation (corrected) of the results " + str(round(var**0.5, 2)) + " seconds")
        times.remove(max(times))
        print("Average time required not considering the worst iteration: " + str(round(sum(times)/(self.iterations-1), 3)) + " seconds")


    
    def run_ls_from_kron(self):
        times = []
        solutions = []

        for i in range(self.iterations):
            starting_time = time()
            s1 = Kronecker(self.queens, 'GS')
            sol1 = s1.solve()
            s2 = LocalSearchSolver(sol1)
            sol2 = s1.solve()
            times.append(time() - starting_time)
            if sol2.is_a_solution():
                solutions.append(1)
            else:
                solutions.append(0)

        m = round(sum(times) / self.iterations, 3)
        var = sum([(i - m)**2 for i in times]) / (self.iterations - 1)
        
        print("\nLOCAL SEARCH FROM KRON BENCHMARK: queens = {}, iterations = {}\n".format(self.queens,self.iterations))
        print("Total time required " + str(round(sum(times), 2)) + " seconds")
        print("Average time required: " + str(m) + " seconds")
        print("Time taken by the worst iteration: " + str(round(max(times), 2)) + " seconds")
        print("Number of actual solutions = {} out of {}  ({}%)".format(sum(solutions), self.iterations, round(sum(solutions)/self.iterations * 100, 2)))
        print("Standard deviation (corrected) of the results " + str(round(var**0.5, 2)) + " seconds")
        times.remove(max(times))
        print("Average time required not considering the worst iteration: " + str(round(sum(times)/(self.iterations-1), 3)) + " seconds")

    

    def __init__(self, n, it):
        self.queens = n
        self.iterations = it


    def run(self):
        # cpb
        self.run_cpb()
        print('\n')
        
        # local
        self.run_local()
        print('\n')
        
        # global
        self.run_global()
        print('\n')

        # kronecker with global search
        self.run_kronecker()
        print('\n')

        # kronecker with constraint propagation
        self.run_kronecker('CP')
        print('\n')

        # global search from kronecker solved with global search
        self.run_gs_from_kron()
        print('\n')

        # local search from kronecker solved with global search
        self.run_ls_from_kron()
        print('\n')






    


