import time
from PatternSolver import PatternSolver


pattern_solver = PatternSolver()
start_time = time.perf_counter()
result = pattern_solver.brute_dfs(4)
end_time = time.perf_counter()
print(f"Ellapsed {round(end_time - start_time,2)} seconds")