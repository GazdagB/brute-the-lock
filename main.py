import time
from PatternSolver import PatternSolver


pattern_solver = PatternSolver()
start_time = time.perf_counter()
result = pattern_solver.brute_bfs(1,1, True)
end_time = time.perf_counter()
print(f"Time: {round(end_time - start_time,3)} seconds")
print(f"Possible Outcomes: {len(result)}")
