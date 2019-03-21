# N-Queens solvers
Assignment for the course of **Artificial Intelligence - Knowledge Representation and Planning**, Prof. Andrea Torsello, Ca' Foscari University of Venice, A.Y. 2018-2019.

## Solvers
Three solvers are implemented:
* Constraint Propagation and Backtracking
* Local Search (Hill Climbing)
* Global Search (Simulated Annealing)

## Running the code
`./Runner.py`

You can either pass the number of queens and the repetitions as command line arguments or once you have run the code.
For instance, `./Runner.py 10 5` runs all the solvers (CPB, LS, GS, Kronecker, ...) 5 times on a 10x10 board and returns the results of the test. Otherwise, you can simply run `./Runner.py` and then type the number of queens and the number of iterations.

### Available tests
The tests run are:
* Constraint Propagation and Backtracking
* Local Search (Hill Climbing)
* Global Search (Simulated Annealing)
* Kronecker using Global Search
* Kronecker using Constraint Propagation
* Global Search from Kronecker (with Kronecker solved using GS)
* Local Search from Kronecker (with Kronecker solved using GS)

These tests can be run from a `Benchmark` object, specifically with:
* `run_cpb()`
* `run_local()`
* `run_global()`
* `run_kronecker()`
* `run_kronecker('CP')`
* `run_gs_from_kron()`
* `run_ls_from_kron()`

Calling the `run()` method (which is what the `Runner` does) launches all of the above methods.

### Printing a board

To print a board, just print the solution to a problem. E.g.:

```python
s = GlobalSearchSolver(200)
solution = s.solve()
print(solution)
```


## Further information
For more information, check out the [report](./Report.pdf).
